'''Importing path and views'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('autostores/', views.AutoStoresView.as_view(), name='autostores'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('search/', views.SearchCarsView.as_view(), name='search_cars'),
]
