from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .import views

app_name = 'posts'
urlpatterns = [
  # 영화 디테일 페이지관련
  path('<int:detail_pk>/', views.detail, name='detail'),
  # path('<int:post_pk>/likes/', views.likes, name='likes'),

  # 코멘트 모음 페이지
  path('<int:detail_pk>/comments/', views.comments, name='comments'),

  # 코멘트 페이지 관련
  path('<int:detail_pk>/comments/<int:comment_pk>/', views.comment, name='comment'),
  path('<int:detail_pk>/comment/', views.comment_create, name='comment_create'),
  path('<int:detail_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
  path('<int:detail_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
  path('<int:detail_pk>/comments/<int:comment_pk>/likes/', views.comment_likes, name='comment_likes'),

  # 코멘트 댓글 관련
  path('<int:detail_pk>/comments/<int:comment_pk>/recomments/', views.recomment_create, name='recomment_create'),
  path('<int:detail_pk>/comments/<int:comment_pk>/recomments/<int:recomment_pk>/delete/', views.recomment_delete, name='recomment_delete'),
  path('<int:detail_pk>/comments/<int:comment_pk>/recomments/<int:recomment_pk>/update/', views.recomment_update, name='recomment_update'),
  path('<int:detail_pk>/comments/<int:comment_pk>/recomments/<int:recomment_pk>/likes/', views.recomment_likes, name='recomment_likes'),

  # 검색 페이지 관련
  path('search/', views.search, name='search'),

  # 가짜 어드민 페이지
  re_path(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
]