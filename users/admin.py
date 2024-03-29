""" User admin classes. """
# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture', 'get_following')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number',)

    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'picture')
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                'biography',
                'following'
            )
        }),
        ('Metadata', {
            'fields': ('created', 'modified')
        })
    )

    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
