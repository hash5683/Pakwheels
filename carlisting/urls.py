'''imprting path and views'''

from django.urls import path
from . import views

urlpatterns = [ 
    path('create/', views.create_car_listing, name='create_car_listing'), 
    path('car_listing_success', views.car_listing_success , name='car_listing_success'),\
    path('', views.car_listing , name='home'),\
    path('view-listed-cars/', views.view_listed_cars, name='view_listed_cars'),
    path('all-listings/', views.all_car_listings, name='all_car_listings'),
]
