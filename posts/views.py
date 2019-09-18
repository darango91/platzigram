"""Posts views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


class PostsDetailView(LoginRequiredMixin, DetailView):
    """Return post detail"""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create new post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super(**kwargs).get_context_data()
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile

        return context
