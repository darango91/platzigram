"""Users URLs"""
# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # Management
    path(
        route='login/',
        view=views.UserLoginView.as_view(),
        name='login'
    ),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.UserSignUp.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UserUpdate.as_view(),
        name='update'
    ),

    path(
        route='follow/',
        view=views.follow_view,
        name='follow'
    ),

    path(
        route='unfollow/',
        view=views.unfollow_view,
        name='unfollow'
    ),

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]