from django.urls import path, re_path
from django.views.generic import TemplateView

from .import views

app_name = 'posts'
urlpatterns = [
  path('', views.post_list,name='index'),
  path('<int:pk>/', views.post_detail,name='detail'),
  # path('search/',TemplateView.as_view(template_name='post_search.html'), name='search'),
  # path('/',views.index, name='index'),
]