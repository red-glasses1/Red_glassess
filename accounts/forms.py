# from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Profile


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['nickname','photo','follower_set']
    widgets = {
      'follower_set' : forms.Select,
    }



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)