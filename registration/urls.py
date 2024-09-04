'''imprting path and views'''
from django.urls import path
from . import views

app_name = 'registeration'

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    # Add other paths as needed
]
