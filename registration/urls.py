'''imprting path and views'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_signup, name='signup'),
    # Add other paths as needed
]