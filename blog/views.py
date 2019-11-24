from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Tag, Post, Comment

# Create your views here.
class HomeView(View):
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        context = {"categories": category_list, "post_list": post_list}
        return render(request, "blog/post_list.html", context)


class CategoryView(View):
    #Вывод статей категорий
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        context = {"category": category}
        return render(request, "blog/post_list.html", context)

class PostDetailView(View):
    #Вывод полной статьи по ссылке
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        context = {"categories": category_list, "post": post}
        return render(request, "blog/post_detail.html", context)