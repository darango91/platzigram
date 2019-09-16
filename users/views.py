""" User views. """

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Models
from users.models import Profile
from django.contrib.auth.models import User

# Exceptions
from django.db.utils import IntegrityError


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


@login_required()
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_conf = request.POST['passwd_confirmation']

        if passwd != passwd_conf:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        else:
            try:
                user = User.objects.create_user(username=username, password=passwd)
            except IntegrityError:
                return render(request, 'users/signup.html', {'error': 'Username {0} already exists'.format(username)})

            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

            profile = Profile(user=user)
            profile.save()

            return redirect('login')

    return render(request, 'users/signup.html')


@login_required()
def update_profile(request):
    """Update a user's profile view"""
    return render(request, 'users/update_profile.html')
