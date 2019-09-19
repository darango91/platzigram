""" Users models """
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model
    Proxy model that extends the base data with other information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    following = models.ManyToManyField(
        'self',
        related_name='followees',
        symmetrical=False
    )

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_following_list(self):
        followings = ''
        if self.following.count() > 0:
            for p in self.following.all():
                followings = followings + p.user.username + ", "
        return followings

    def get_followers_list(self):
        followers = Profile.objects.filter()
        return None