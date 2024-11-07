from django.urls import path
from . import views

urlpatterns = [
    path('',views.first_app,name='first_app'),
]
