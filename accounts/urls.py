from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('profile/edit/', views.profile_edit, name='profile_edit'),
  path('password_change/',views.password_change, name='password_change'),
  path('<str:username>/profile/', views.profile_detail, name='profile'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('delete/', views.delete, name='delete'),
  path('<str:username>/follower/', views.follow, name='follow'),
]
