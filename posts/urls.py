from django.urls import path, re_path
from django.views.generic import TemplateView

from .import views

app_name = 'posts'
urlpatterns = [
  path('', views.post_list, name='index'),
  # path('<int:pk>/', views.post_detail, name='detail'),
  path('detail/', views.detail, name='detail'),
  path('comments/', views.comments, name='comments'),
  path('comment/', views.comment, name='comment'),
  path('search/', views.search, name='search'),
  # path('search/',TemplateView.as_view(template_name='post_search.html'), name='search'),
  # path('/',views.index, name='index'),
]