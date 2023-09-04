from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from posts.models import Post, Comment

admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'photo', 'author_link']
    list_editable = ['title', 'text', 'photo']
    list_filter = ['created']

    def author_link(self, obj) -> str:
        return format_html(
            "<a href='{url}'>{user_name}</a>",
            url=reverse('admin:users_user_change', kwargs={'object_id': obj.author.id}),
            user_name=obj.author.username
        )
    author_link.short_description = 'Автор'
