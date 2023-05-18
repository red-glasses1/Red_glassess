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

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title','image','content','score','like_users','released_at']
#         widgets = {
#             'content' : forms.Textarea
#         }
