'''views for app carlisting'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Carlisting
from .forms import CarForm

@login_required
def create_car_listing(request):
    '''crreate listings for cars'''
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car_listing = form.save(commit=False)
            car_listing.user = request.user  # Set the user to the current logged-in user
            car_listing.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'createlisting.html', {'form': form})

def car_listing_success(request):
    '''car listing success'''
    return render(request, 'home.html')

def car_listing(request):
    '''car listing'''
    # Fetch all car listings
    cars_list = Carlisting.objects.all().order_by('-date_added')[:6]
    return render(request, 'home.html', {'cars_list': cars_list})


@login_required
def view_listed_cars(request):
    '''View listed cars'''
    # This code will only be executed if the user is authenticated
    user_cars = Carlisting.objects.filter(user=request.user)
    return render(request, 'viewlistedcars.html', {'user_cars': user_cars})

def all_car_listings(request):
    '''View all car listings'''
    # Fetch all car listings
    all_cars = Carlisting.objects.all().order_by('-date_added')
    return render(request, 'all_listings.html', {'all_cars': all_cars})

