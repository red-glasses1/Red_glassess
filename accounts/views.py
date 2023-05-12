import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from pyexpat.errors import messages
from accounts.forms import ProfileForm
from accounts.models import Profile
from django.conf import settings

User = get_user_model()

# Create your views here.
signup = CreateView.as_view(
  model=User,
  success_url = reverse_lazy('posts:index'),
  form_class=UserCreationForm,
  template_name='signup_form.html'
)
@login_required
def profile_edit(request):
  # profile = get_object_or_404(Profile)  # = Profile.objects.get(user=request.user)
  try: # 프로필이 있으면
    profile = request.user.profile
  except Profile.DoesNotExist: # 없으면
    profile = None

  if request.method == "POST":
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      form.save()
      messages.info(request,'프로필 수정이 완료되었습니다.')
      return redirect('accounts:profile')
  else:
    form = ProfileForm(instance=profile)
    return render(request,'profile_edit.html',{'form':form,'profile':profile})

class ProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'profile.html'

profile = ProfileView.as_view()