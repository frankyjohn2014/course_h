# from django import forms
# from scraping.models import Category, Language, Post, Post_video

# class FindForm(forms.Form):
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='slug', 
#     required=False, widget=forms.Select(attrs={'class':'form-control'}), label='Категория')

#     language = forms.ModelChoiceField(queryset=Language.objects.all(), to_field_name='slug',
#     required=False, widget=forms.Select(attrs={'class':'form-control'}), label='Язык программирования')
    
# class VForm(forms.ModelForm):
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#     widget=forms.Select(attrs={'class':'form-control'}), label='Категория')

#     language = forms.ModelChoiceField(queryset=Language.objects.all(),
#     widget=forms.Select(attrs={'class':'form-control'}), label='Язык программирования')
#     url = forms.URLField(label='Url', widget=forms.URLInput(attrs={'class':'form-control'}))
#     title = forms.CharField(label='Заголовок вакансий', widget=forms.TextInput(attrs={'class':'form-control'}))
#     company = forms.CharField(label='Компания',widget=forms.TextInput(attrs={'class':'form-control'}))
#     description = forms.CharField(label='Описание поста',widget=forms.Textarea(attrs={'class':'form-control'}))
#     post_video = forms.ModelChoiceField(queryset=Post_video.objects.all(),
#     widget=forms.Select(attrs={'class':'form-control'}), label='Ссылки видео')

#     class Meta:
#         model = Post
#         fields = '__all__'
