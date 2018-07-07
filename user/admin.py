from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    """
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()        
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    """

admin.site.unregister(User)
admin.site.register(User, UserAdmin)