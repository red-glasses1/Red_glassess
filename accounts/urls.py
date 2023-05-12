from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts import views
app_name = 'accounts'
urlpatterns = [
  path('signup/',views.signup,name='signup'),
  path('profile/edit/',views.profile_edit, name='profile_edit'),
  path('profile/',views.profile,name='profile'),
  path('login/',LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', LogoutView.as_view(),name='logout'),
]
