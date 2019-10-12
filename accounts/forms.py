from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class ProfileForm(UserCreationForm):
 
    class Meta:
        model = Profile
        fields = ('phone_number','profile_picture', 'gender', 'date_of_birth')
