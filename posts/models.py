from django.db import models

from compost.models import BaseModel
from users.models import User


class Post(BaseModel):

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = models.CharField(verbose_name="Содержание", max_length=500)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title


class Comment(BaseModel):

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    text = models.CharField(verbose_name="Содержание", max_length=200)
    commentator = models.ForeignKey(User, verbose_name="автор", on_delete=models.CASCADE, related_name='commentator')
    post = models.ForeignKey(Post, verbose_name="пост", on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.text
