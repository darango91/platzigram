"""Posts views."""

# Django
from typing import List, Any

from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Yessica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1036/200/200',
    },
    {
        'name': 'Via Lactea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/903/200/200',
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Thepianistartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1076/200/200',
    }
]


# Create your views here.
def list_posts(request):
    """List existing posts."""
    posts_list = [1, 2, 3, 4]
    content: List[Any] = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))

    return HttpResponse('<br>'.join(content))
