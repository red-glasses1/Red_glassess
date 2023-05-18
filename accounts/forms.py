# from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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
        ),
        required=False,
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'image')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)


class CustomPasswordChangeForm(PasswordChangeForm):
        old_password = forms.CharField(
        label='기존 비밀번호',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-100 p-2 mb-2',
                'type': 'password',
            },
        ),
    )
        new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-100 p-2 mb-2',
                'type': 'password',
            },
        ),
    )
        new_password2 = forms.CharField(
        label='새 비밀번호(확인)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-100 p-2 mb-2',
                'type': 'password',
            },
        ),
    )
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2',)
