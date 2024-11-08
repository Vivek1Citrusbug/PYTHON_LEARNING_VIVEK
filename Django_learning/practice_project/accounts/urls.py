from django.urls import path
from . import views

urlpatterns = [
    path('registration/register',views.registration, name='regisernewuser'),
]
