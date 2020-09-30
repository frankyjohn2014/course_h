from django.shortcuts import render
from .models import Post,Post_video
# from .forms import FindForm,VForm
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib import messages

# def home_view(request):
#     print(request.GET)
#     form = FindForm()
#     return render(request,'scraping/home.html', {'form':form})


# def list_view(request):
#     # print(request.GET)
#     form = FindForm()
#     category = request.GET.get('category')
#     language = request.GET.get('language')
#     page_obj = []
#     context = {'category': category, 'language':language, 'form':form}

#     if category or language:
#         _filter = {}
#         if category:
#             _filter['category__slug'] = category
#         if language:
#             _filter['language__slug'] = language
#         qs = Category.objects.filter(**_filter).select_related('category','language')

#         paginator = Paginator(qs, 10) # Show 25 contacts per page.

#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context['object_list'] = page_obj
#     return render(request,'scraping/list.html', context)


class DView(DetailView):
    queryset = Post.objects.all()
    template_name = 'scraping/detail_view.html'

class VList(ListView):
    model = Post
    template_name = 'scraping/home.html'
    # form = FindForm() 
    # paginate_by = 6
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category'] = self.request.GET.get('category')
    #     context['language'] = self.request.GET.get('language')
    #     context['form'] = self.form
    #     return context
    
    # def get_queryset(self, **kwargs):
    #     category = self.request.GET.get('category')
    #     language = self.request.GET.get('language')
    #     qs = []
    #     if category or language:
    #         _filter = {}
    #         if category:
    #             _filter['category__slug'] = category
    #         if language:
    #             _filter['language__slug'] = language
    #         qs = Category.objects.filter(**_filter).select_related('category','language')
    #     return qs

# class VCreate(CreateView):
#     model = Post
#     # fields = '__all__'
#     form_class = VForm
#     template_name = 'scraping/create_view.html'
#     success_url = reverse_lazy('home')

# class VUpdate(UpdateView):
#     model = Post
#     # fields = '__all__'
#     form_class = VForm
#     template_name = 'scraping/create_view.html'
#     success_url = reverse_lazy('home')

# class VDelete(DeleteView):
#     model = Post
#     template_name = 'scraping/delete.html'
#     success_url = reverse_lazy('home')

#     # удаление без запроса подтверждения
#     def get(self, request, *args,**kwargs):
#         messages.success(request, 'Пост успешно удалён')
#         return self.post(request,*args,**kwargs)