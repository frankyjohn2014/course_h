from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from .forms import UserLoginForm,UserRegistrationForm,UserUpdateForm,ContactForm
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib import messages 
from scraping.models import Error
import datetime as dt
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
import django
import datetime
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from scraping_service.settings import EMAIL_HOST_USER

User = get_user_model()

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        messages.success(request, 'Вы успешно зарегистрированы')
        return render(request, 'accounts/register_done.html',{'new_user':new_user})
    return render(request, 'accounts/register.html',{'form':form})

def update_view(request):
    contact_form = ContactForm()
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.category = data['category']
                user.language = data['language']
                user.send_email = data['send_email']
                user.save()
                messages.success(request, 'Данные сохранены.')
                return redirect('accounts:update')

        form = UserUpdateForm(initial={'category': user.category, 
        'language': user.language, 'send_email':user.send_email})
        return render(request, 'accounts/update.html',
        {'form':form, 'contact_form':contact_form})
    else:
        return redirect('accounts:login')

def delete_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            qs = User.objects.get(pk=user.pk)
            qs.delete()
            messages.error(request, 'Пользователь удалён :(')

    return redirect('home')

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            category = data.get('category')
            language = data.get('language')
            email = data.get('email')
            qs = Error.objects.filter(timestamp=dt.date.today())
            if qs.exists:
                err = qs.first()
                data = err.data.get('user_data',[])
                data.append({'category': category,'language':language,'email':email})
                err.data['user_data'] = data
                err.save()
            else:
                data = [{'category': category,'language':language,'email':email}]
                Error(data=f"user_data:{data}").save()
            messages.success(request,'Данные отправлены администрации')
            return redirect('accounts:update')
        else:
            return redirect('accounts:update')
    else:
        return redirect('accounts:login')

def reg_email(request):
    if request.method == 'POST':
        contact_form = UserRegistrationForm(request.POST or None)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            email = data.get('email')
            from_email = EMAIL_HOST_USER
            _html = '<h1>html</h1>'
            to = email
            messages.success(request,'Letter send to you email')
            msg = EmailMultiAlternatives('Здравствуйте, вы успешно зарегестрированы на сайте recourse_hunter, ', 'Здравствуйте, вы успешно зарегестрированы на сайте recourse_hunter', from_email, [to])
            # msg.attach_alternative(_html, "text/html")
            msg.send()
            return redirect('accounts:success')
        else:
            return redirect('accounts:update')
    else:
        return redirect('accounts:login')

def success(request):
    email = request.POST.get('email', '')
    data = """
Hello there!

I wanted to personally write an email in order to welcome you to our platform.\
 We have worked day and night to ensure that you get the best service. I hope \
that you will continue to use our service. We send out a newsletter once a \
week. Make sure that you read it. It is usually very informative.

Cheers!
~ Yasoob
    """
    send_mail('Welcome!', data, "Yasoob",
              [email], fail_silently=False)
    return render(request, 'accounts/success.html')
