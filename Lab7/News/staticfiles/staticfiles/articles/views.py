from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = 'comment_new.html'
    fields = ['comment', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article_id = self.kwargs.get(self.pk_url_kwarg)
        return super().form_valid(form)

