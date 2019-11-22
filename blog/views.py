from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Tag, Post, Comment

# Create your views here.
class HomeView(View):
    def get(self, request):
        category_list = Category.objects.all()
        posts = Post.objects.all()
        context = {"categories": category_list, "posts": posts}
        return render(request, "blog/home.html", context)


class CategoryView(View):
    #Вывод статей категорий
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        context = {"category": category}
        return render(request, "blog/post_list.html", context)

class PostView(View):
    #Вывод поста по ссылке
    def get(self, request, post_slug):
        #category = Category.objects.get(slug=category_slug)
        post = Post.objects.get(slug=post_slug)
        context = {"post": post}
        return render(request, "blog/post.html", context)