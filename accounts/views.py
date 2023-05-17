import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from pyexpat.errors import messages
# from accounts.forms import ProfileForm
# from accounts.models import Profile
from django.conf import settings

# User = get_user_model()

# Create your views here.
# signup = CreateView.as_view(
#   model=User,
#   success_url = reverse_lazy('posts:index'),
#   form_class=UserCreationForm,
#   template_name='signup_form.html'
# )

# @login_required
# def profile_edit(request):
#     # profile = get_object_or_404(Profile)  # = Profile.objects.get(user=request.user)
#     try: # 프로필이 있으면
#         profile = request.user.profile
#     except Profile.DoesNotExist: # 없으면
#         profile = None

#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             form.save()
#             messages.info(request,'프로필 수정이 완료되었습니다.')
#         return redirect('accounts:profile')
#     else:
#         form = ProfileForm(instance=profile)
#         return render(request,'profile_edit.html',{'form':form,'profile':profile})

# class ProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'profile.html'

# profile = ProfileView.as_view()


def profile(request, username):
    person = get_user_model().objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


def login(request):
    next = request.GET.get('next')
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(next)
        else:
            return render(request, 'index.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'index.html', {'next': next})


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('index')


def signup(request):
    next = request.GET.get('next')
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            return redirect(next)
        else:
            return render(request, 'index.html', {'error': 'username or password is incorrect'})
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

@login_required
def user_follow(request,nickname):
  follow_user = get_object_or_404(get_user_model(),nickname=nickname,is_active=True)
  request.follow_user.follower_set.add(follow_user)
  follow_user.follower_set.add(request.user)
  redirect_url = request.META.get("HTTP_REFERER",'index')
  return redirect(redirect_url,nickname=nickname)

@login_required
def user_unfollow(request,nickname):
  follow_user = get_object_or_404(get_user_model(),nickname=nickname,is_active=True)
  request.follow_user.remove(follow_user)
  follow_user.follower_set.remove(request.user)
  redirect_url = request.META.get("HTTP_REFERER",'index')
  return redirect(redirect_url,nickname=nickname)