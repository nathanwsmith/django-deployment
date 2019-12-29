from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
]