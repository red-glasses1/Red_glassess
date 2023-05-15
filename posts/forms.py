from django import forms
from .models import Post, Comment, Recomment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class RecommentForm(forms.ModelForm):
    class Meta:
        model = Recomment
        fields = ('content',)