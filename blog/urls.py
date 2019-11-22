from django.urls import path

from . import views

urlpatterns = [
    path('category/<slug:category_slug>/', views.CategoryView.as_view(), name="category"),
    path('<slug:post_slug>/', views.PostView.as_view(), name="post"),
    path("", views.HomeView.as_view()),
]