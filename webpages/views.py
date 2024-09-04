from django.shortcuts import render
from django.views import View
from django.db.models import Q
from carlisting.models import CarListing

class HomePageView(View):
    '''Class-based view for the home page'''

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class SearchCarsView(View):
    '''Class-based view for searching car listings'''

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        city = request.GET.get('city', '')
        price_range = request.GET.get('price_range', '')

        # Start with all car listings
        car_listings = CarListing.objects.all()

        # Filter by query in make, carname, or description
        if query:
            car_listings = car_listings.filter(
                Q(car_name__icontains=query) | 
                Q(make__icontains=query) | 
                Q(description__icontains=query)
            )
        
        # Filter by city (assuming there is a city field in Carlisting)
        if city and city != 'All Cities':
            car_listings = car_listings.filter(city__iexact=city)

        # Filter by price range (assuming the format is "min-max")
        if price_range:
            try:
                min_price, max_price = map(float, price_range.split('-'))
                car_listings = car_listings.filter(price__gte=min_price, price__lte=max_price)
            except ValueError:
                pass  # Handle invalid price range input

        context = {
            'car_listings': car_listings,
            'query': query,
            'price_range': price_range
        }
        return render(request, 'home.html', context)


class ListedCarsView(View):
    '''Class-based view for the list of cars page'''

    def get(self, request, *args, **kwargs):
        return render(request, 'cars.html')


class ServicesView(View):
    '''Class-based view for the services page'''

    def get(self, request, *args, **kwargs):
        return render(request, 'services.html')


class BlogsView(View):
    '''Class-based view for the blogs page'''

    def get(self, request, *args, **kwargs):
        return render(request, 'blogs.html')


class AutoStoresView(View):
    '''Class-based view for the auto stores page'''

    def get(self, request, *args, **kwargs):
        return render(request, 'store.html')


class AboutView(View):
    '''Class-based view for the about page'''

    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class ContactView(View):
    '''Class-based view for the contact page'''

    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')
