'''views for app carlisting'''
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from carlisting.models import CarListing
from .forms import CarForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class CreateCarListingView(LoginRequiredMixin, View):
    '''Class-based view to create car listings'''

    def get(self, request, *args, **kwargs):
        '''Handles GET requests to show the car listing form'''
        form = CarForm()
        return render(request, 'createlisting.html', {'form': form})

    def post(self, request, *args, **kwargs):
        '''Handles POST requests to submit the car listing form'''
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car_listing = form.save(commit=False)
            car_listing.user = request.user  # Set the user to the current logged-in user
            car_listing.save()
            return redirect('home')
        return render(request, 'createlisting.html', {'form': form})


class CarListingSuccessView(View):
    '''Class-based view for car listing success page'''

    def get(self, request, *args, **kwargs):
        '''Handles GET requests to show the success page'''
        return render(request, 'home.html')


class CarListingView(View):
    '''Class-based view to display car listings on the home page with pagination'''

    def get(self, request, *args, **kwargs):
        '''Handles GET requests to fetch and display car listings with pagination'''
        cars_list = CarListing.objects.all().order_by('-date_added')
        
        # Set up pagination
        paginator = Paginator(cars_list, 6)  # Display 6 cars per page
        page = request.GET.get('page')
        
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            cars = paginator.page(1)  # If page is not an integer, show the first page
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)  # If page is out of range, show the last page
        
        return render(request, 'home.html', {'cars_list': cars})


class ViewListedCarsView(LoginRequiredMixin, View):
    '''Class-based view to display cars listed by the logged-in user'''

    def get(self, request, *args, **kwargs):
        '''Handles GET requests to show user's listed cars'''
        user_cars = CarListing.objects.filter(user=request.user)
        return render(request, 'viewlistedcars.html', {'user_cars': user_cars})


class AllCarListingsView(View):
    '''Class-based view to display all car listings'''

    def get(self, request, *args, **kwargs):
        '''Handles GET requests to fetch and display all car listings'''
        all_cars = CarListing.objects.all().order_by('-date_added')
        return render(request, 'all_listings.html', {'all_cars': all_cars})
