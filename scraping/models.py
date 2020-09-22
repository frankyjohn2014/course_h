from django.db import models
from .utils import from_cyrillic_to_eng
import jsonfield

def default_urls():
    return {"tut_pars": "", "bel_pars":""}



class Category(models.Model):
    name = models.CharField(max_length=50,unique=True, verbose_name='Название категории')
    slug = models.CharField(max_length=50,unique=True, blank=True)

    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Название категорий'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args,**kwargs)    

class Language(models.Model):
    name = models.CharField(max_length=50,unique=True, verbose_name='Язык программирования',blank=True, null=True)
    slug = models.CharField(max_length=50,unique=True, blank=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args,**kwargs) 

class Post(models.Model):
    title = models.CharField(max_length=250,verbose_name='Заголовок поста')
    # url = models.URLField(unique=True)
    # company = models.CharField(max_length=250,verbose_name='Компания')
    # description = models.TextField(verbose_name='Описание курса')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык программирования')
    # post_video = models.ManyToManyField(Post_video)
    timestamp = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-timestamp']

    def __str__(self):
        return self.title
        
class Post_video(models.Model):
    title = models.CharField(max_length=300,verbose_name='Название видео', blank=True, null=True)
    videos = models.URLField(unique=True, blank=True, null=True)
    posts = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Пост', blank=True, null=True)
    category1 = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    class Meta:
        verbose_name = 'Ссылка видео'
        verbose_name_plural = 'Ссылки видео'

    def __str__(self):
        return self.title
class Error(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    data = jsonfield.JSONField()

    def __str__(self):
        return str(self.timestamp)

# class Url(models.Model):
#     category = models.ForeignKey('Сategory', on_delete=models.CASCADE, verbose_name='Город')
#     language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык программирования')
#     url_data = jsonfield.JSONField(default=default_urls)

#     class Meta:
#         unique_together = ("category", "language") 