from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from . import models


class ArticleListView(ListView):
    paginate_by = 5
    model = models.Article
    template_name = 'articles/article_list.html'

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        if sort is None: sort = 'date'
        if sort == 'author': sort = 'author__username'
        return models.Article.objects.order_by(sort).select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        sort = self.request.GET.get('sort')
        if sort is None: sort = 'date'
        data['sort'] = sort
        return data

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'articles/article_detail.html'
    queryset = models.Article.objects.all().prefetch_related('comments__author')


    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            comment = self.request.POST.get('comment')
            new_comment = models.Comment.objects.create(comment=comment,
                                                       article=self.get_object(),
                                                       author=self.request.user)
            new_comment.save()
            return redirect(self.request.path_info)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'articles/article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'articles/article_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'articles/article_new.html'
    fields = ['title', 'body', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SearchResultsListView(ListView):
    paginate_by = 5
    models = models.Article
    template_name = 'articles/search_result.html'

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        if sort is None: sort = 'date'
        if sort == 'author': sort = 'author__username'
        query = self.request.GET.get("q")
        return models.Article.objects.filter(
            Q(title__icontains=query) |
            Q(author__username__icontains=query) |
            Q(body__icontains=query)
        ).order_by(sort).select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        sort = self.request.GET.get('sort')
        query = self.request.GET.get("q")
        if sort is None: sort = 'date'
        data['sort'] = sort
        data['query'] = query
        return data