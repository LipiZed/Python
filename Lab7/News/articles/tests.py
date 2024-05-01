from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .models import Article, Comment
from .views import *

class ArticleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='test_user',
            password='test1234',
            email='test@mail.ru'
        )
        cls.article = Article.objects.create(
            title='test_article',
            body='test_body',
            author=cls.user
        )
        cls.comment = Comment.objects.create(
            article=cls.article,
            comment='test_comment',
            author=cls.user
        )

    def test_information(self):
        self.assertEqual(self.article.title, 'test_article')
        self.assertEqual(self.article.body, 'test_body')
        self.assertEqual(self.article.author.username, 'test_user')
        self.assertEqual(Article.objects.all().count(), 1)
        self.assertEqual(Comment.objects.all().count(), 1)
        self.assertEqual(self.user.email, 'test@mail.ru')
        self.assertIs(self.user, self.article.author)
        self.assertIs(self.user, self.comment.author)
        self.assertEqual(self.comment.comment, 'test_comment')

    def test_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_list.html')

    def test_detail_view(self):
        response = self.client.get(self.article.get_absolute_url())
        fake_response = self.client.get('books/999')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(fake_response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_detail.html')

    def test_buttons_edit_delete_update_for_login(self):
        self.client.login(username='test_user', password="test1234")
        response = self.client.get(self.article.get_absolute_url())
        self.assertContains(response, 'Edit')
        self.assertContains(response, 'Delete')
        self.assertContains(response, 'Add a new comment')

    def test_buttons_edit_delete_update_for_unlogin(self):
        response = self.client.get(self.article.get_absolute_url())
        self.assertNotContains(response, 'Edit')
        self.assertNotContains(response, 'Delete')
        self.assertNotContains(response, 'Add a new comment')

    def test_paginate(self):
        response = self.client.get(reverse('article_list'))
        self.assertContains(response, 'Page 1 of 1')