from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import JsonResponse


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
@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/password_change.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('index')


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
