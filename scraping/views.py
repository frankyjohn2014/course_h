from django.shortcuts import render
from .models import Post,Post_video
# from .forms import FindForm,VForm
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.db.models import Q


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


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    # queryset = Post.objects.filter(title__icontains='Angular')
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(descr_post__icontains=query) | Q(desc_large__icontains=query)
        )
        return object_list
