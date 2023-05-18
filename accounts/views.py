import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from pyexpat.errors import messages
from accounts.models import Profile
from django.contrib.auth.views import PasswordChangeView as AuthPasswordChangeView
# from accounts.forms import ProfileForm
# from accounts.models import Profile
from django.conf import settings
from django.http import JsonResponse


# 프로필 수정
@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', username=request.user.username)
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request,'accounts/profile_edit.html', context)

# 비밀번호 수정
class PasswordChangeView(LoginRequiredMixin,AuthPasswordChangeView):
  success_url = reverse_lazy('index:root')
  template_name = 'accounts/password_change_form.html'
  # 중복 비밀번호에 대한 검사
  form_class = PasswordChangeForm
  # 자체 뷰에서도 form_valid가 있으므로 부모의 메서드를 가져오게 되면 초기화를 해줘야 한다.(super())
  def form_valid(self,form):
    messages.success(self.request,'암호를 변경했습니다.')
    return super().form_class(form)

password_change = PasswordChangeView.as_view()

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

profile = ProfileView.as_view()


def profile_detail(request, username):
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
            return render(request, 'index.html', {'error': '아이디 또는 비밀번호가 올바르지 않습니다.'})
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
            return render(request, 'index.html', {'error': '아이디 또는 비밀번호가 올바르지 않습니다.'})
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('index')


@login_required
def user_follow(request):
  follow_user = get_object_or_404(get_user_model(),nickname=request.user.username,is_active=True)
  request.follow_user.follower_set.add(follow_user)
  follow_user.follower_set.add(request.user.username)
  redirect_url = request.META.get("HTTP_REFERER",'index')
  return redirect(redirect_url,nickname=request.user.username)

@login_required
def user_unfollow(request):
  follow_user = get_object_or_404(get_user_model(),nickname=request.user.username,is_active=True)
  request.follow_user.remove(follow_user)
  follow_user.follower_set.remove(request.user.username)
  redirect_url = request.META.get("HTTP_REFERER",'index')
  return redirect(redirect_url,nickname=request.user.username)

@login_required
def follow(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)

    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
            is_followed = False
        else:
            person.followers.add(request.user)
            is_followed = True
        context = {
            'is_followed' : is_followed,
            'followings_count': person.followings.count(),
            'followers_count': person.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', person.username)
