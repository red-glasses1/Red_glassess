from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path
from accounts import views

app_name = 'accounts'
urlpatterns = [
  path('signup/', views.signup, name='signup'),
  # path('profile/edit/', views.profile_edit, name='profile_edit'),
  path('<str:username>/profile/', views.profile, name='profile'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  re_path(r'^(?P<nickname>[\w.@+-]+)/follow/$', views.user_follow,name='user_follow'),
  re_path(r'^(?P<nickname>[\w.@+-]+)/unfollow/$',views.user_unfollow,name='user_unfollow'),
]
