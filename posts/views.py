from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView

from posts.models import Post


# Create your views here.

# 메인 페이지 (포스팅된 리스트 나열), 검색기능 구현 - FBV
def post_list(request):
  qs = Post.objects.all()
  q = request.GET.get('q','')
  if q:
    qs = qs.filter(Q(title__icontains=q) & Q(content__icontains=q)) # 모델의 타이틀 속성 중에 q 인자에 삽입된 값 을 검색
  return render(request,'post_search.html',{'qs': qs,'q':q})

# 영화 정보 페이지
# post_detail = DetailView.as_view(model=Post,pk_url_kwarg='pk',template_name='post_detail.html')

def detail(request):
  return render(request, 'detail.html')


def comments(request):
  return render(request, 'comments.html')


def comment(request):
  return render(request, 'comment.html')


def search(request):
  return render(request, 'search.html')