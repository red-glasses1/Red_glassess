from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from posts.models import Post, Comment
from .forms import CommentForm, RecommentForm, PostForm
import requests


# Create your views here.
# 포스트 생성
@login_required
def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      # 모델에 작성할 수도 있음
      # for tag_name in post.extract_tag_list():
      #   tag, _ = Tag.objects.get_or_create(name='tag_name')
      post.tag_set.add(*post.extract_tag_list())
      messages.info(request, '포스팅을 저장했습니다.')
      return redirect('/')
  else:
    # get 요청일때
    form = PostForm()
  return render(request, 'post_form.html',{
    'form':form
  })
# 메인 페이지 (포스팅된 리스트 나열), 검색기능 구현 - FBV
def post_list(request):
  qs = Post.objects.all()
  q = request.GET.get('q','')
  if q:
    qs = qs.filter(Q(title__icontains=q) & Q(content__icontains=q)) # 모델의 타이틀 속성 중에 q 인자에 삽입된 값 을 검색
  return render(request,'post_search.html',{'qs': qs,'q':q})


def detail(request, detail_pk):
  # 영화 디테일 정보받기
  detail_url = f"https://api.themoviedb.org/3/movie/{detail_pk}"

  params = {
    "api_key": "6cd101ecd178ac88ad307ea8fccdf574",
    "language": "ko",
    }
    
  detail_response = requests.get(detail_url, params=params)
  detail = detail_response.json()
  genres = detail_response.json()['genres']
  score = round(detail_response.json()['vote_average'], 2)

  # 영화 이미지 받기
  gallery_url = f"https://api.themoviedb.org/3/movie/{detail_pk}/images?api_key=6cd101ecd178ac88ad307ea8fccdf574"

  gallery_response = requests.get(gallery_url)
  gallery = gallery_response.json()['backdrops']

  comments = Comment.objects.filter(pk=detail_pk).order_by('-created_at')

  context = {
    'detail': detail,
    'genres': genres,
    'gallery': gallery,
    'score':score,
    'comments': comments,
  }
  return render(request, 'posts/detail.html', context)


def comments(request, detail_pk):
  comments = Comment.objects.filter(post_id=detail_pk).order_by('-created_at')
  context = {
    'comments': comments,
  }
  return render(request, 'posts/comments.html', context)


def comment(request, detail_pk, comment_pk):
  post = Post.objects.get(pk=detail_pk)
  comment = Comment.objects.filter(pk=comment_pk)
  recomments = comment.recomment_set.all()
  context = {
    'post': post,
    'comment': comment,
    'recomments': recomments,
  }
  return render(request, 'posts/comment.html', context)


@login_required
def comment_create(request, detail_pk):
  post = Post.objects.get(pk=detail_pk)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.user = request.user
      comment.save()
      return redirect('posts:comment', detail_pk=post.pk, comment_pk=comment.pk)
  else:
    form = CommentForm()
  context = {
    'post': post,
    'form': form,
  }
  return render(request, 'posts/detail.html', context)


@login_required
def comment_update(request, detail_pk, comment_pk):
    post = Post.objects.get(pk=detail_pk)
    comment = Comment.objects.get(post_id=detail_pk, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect('posts:comment', detail_pk=post.pk, comment_pk=comment.pk)
        else:
            form = CommentForm(instance=comment)
    else:
        return redirect('posts:comment', detail_pk=post.pk, comment_pk=comment.pk)
    context = {
        'form': form,
        'post': post,
        'comment': comment,
    }
    return render(request, 'posts/detail.html', context)


def search(request):
  return render(request, 'posts/search.html')