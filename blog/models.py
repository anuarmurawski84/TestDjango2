from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50)
    slug = models.SlugField("url", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Post(models.Model):
    title = models.CharField(verbose_name="Имя_поста", max_length=100)
    mini_text = models.TextField(verbose_name="Вступление_поста")
    text = models.TextField(verbose_name="Текст_поста")
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, db_index=True)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    text = models.TextField(verbose_name="Текст_комментария", max_length=200)
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, db_index=True)
    moderation = models.BooleanField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'