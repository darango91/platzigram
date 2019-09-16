"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Utilities
from datetime import datetime

# Forms
from posts.forms import PostForm

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yessica Cortes',
            'picture': 'https://picsum.photos/id/1027/60/60',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1036/800/600'
    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/id/1005/60/60',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/903/800/600',
    },
    {
        'title': 'Nuevo Auditorio',
        'user': {
            'name': 'Thepianistartist',
            'picture': 'https://picsum.photos/id/883/60/60',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1076/800/600',
    },
]

# Create your views here.
@login_required()
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required()
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
