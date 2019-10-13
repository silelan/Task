from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Profile,Address
from django.utils.safestring import mark_safe


admin.site.register(Address)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    data = Profile.objects.all()
    
    for data in data:
        name = data.user.username
        
    print(name)
    readonly_fields = ["profile_picture_preview"]
    search_fields = ('user',)
    list_filter = ('gender','permanent_address')

    def profile_picture_preview(self, obj):
        return mark_safe('<img src="{url}" width="200px" height="200px" />'.format(
            url = obj.profile_picture.url
            )
        )