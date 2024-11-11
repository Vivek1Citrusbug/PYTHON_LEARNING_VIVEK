from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name = ""),
    path('registration/', views.registration_view, name='user-registration'),
    path('login/', views.login_view, name='user-login'),
    path('logout/',views.logout_view, name='user-logout'),
    path('dashboard/', views.dashboard, name="dashboard"),
]
