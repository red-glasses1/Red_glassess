# from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


# class ProfileForm(forms.ModelForm):
#   class Meta:
#     model = Profile
#     fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)