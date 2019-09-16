"""Posts admin classes"""

# Admin
from django.contrib import admin

# models
from django.contrib.auth.models import User
from posts.models import Post


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Posts admin."""
    list_display = ('pk', 'user', 'title', 'photo')
