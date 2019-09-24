""" Users models """
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model
    Proxy model that extends the base data with other information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    relationships = models.ManyToManyField(
        'self',
        through='Follower',
        symmetrical=False,
        related_name='followers'
    )

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def add_follower(self, profile):
        relationship, created = Follower.objects.get_or_create(
            profile_from=self,
            profile_to=profile)
        return relationship

    def remove_relationship(self, person):
        Follower.objects.filter(
            profile_from=self,
            profile_to=person).delete()
        return

    def get_relationships(self):
        return self.relationships.filter(
            to_profile__profile_from=self)

    def get_related_to(self):
        return self.followers.filter(
            from_profile__profile_to=self)

    def get_following(self):
        return self.get_relationships()

    def get_followers(self):
        return self.get_related_to()


class Follower(models.Model):
    profile_from = models.ForeignKey(Profile, related_name='from_profile', on_delete=models.DO_NOTHING)
    profile_to = models.ForeignKey(Profile, related_name='to_profile', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
