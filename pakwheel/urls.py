'''imprting path and views'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage , name='home'),\
    path('services/', views.services , name='services'),\
    path('blogs/', views.blogs , name='blogs'),\
    path('autostores/', views.autostores , name='autostores'),\
    path('about/', views.about , name='about'),\
    path('contact/', views.contact , name='contact'),\
    path('search/', views.search_cars, name='search_cars'),

]