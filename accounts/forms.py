# from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms


class ProfileForm(UserChangeForm):
  username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-100 p-2 mb-2',
                'placeholder': '아이디',
            },
        ),
    )
    
  image = forms.ImageField(
        label='이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            },
        )
    )
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
    fields = ('username', 'photo')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)