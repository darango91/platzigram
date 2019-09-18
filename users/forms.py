# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Signup form"""
    username = forms.CharField(min_length=4, max_length=200)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, widget=forms.EmailInput())

    def clean_username(self):
        """User name must be unique"""
        username = self.cleaned_data["username"]
        username_exists = User.objects.filter(username=username).exists()

        if username_exists:
            raise forms.ValidationError('Username {0} is al ready in use'.format(username))
        return username

    def clean(self):
        """Verify password and confirmation match"""
        data = super().clean()
        password = data['password']
        confirmation = data['password_confirmation']
        if password != confirmation:
            raise forms.ValidationError('Passwords does not match')

        return data

    def save(self):
        """ Create user and profile """
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
