from django.shortcuts import render
from carlisting.models import Carlisting
from django.db.models import Q

def homepage(request):
    '''home page'''
    return render(request, 'home.html')

def search_cars(request):
    query = request.GET.get('q', '')
    city = request.GET.get('city', '')
    price_range = request.GET.get('price_range', '')

    # Start with all car listings
    car_listing = Carlisting.objects.all()

    # Filter by query in make, carname, or description
    if query:
        car_listing = car_listing.filter(
            Q(carname__icontains=query) | 
            Q(make__icontains=query) | 
            Q(description__icontains=query)
        )
    
    # Filter by city (assuming there is a city field in Carlisting)
    if city and city != 'All Cities':
        car_listing = car_listing.filter(city__iexact=city)

    # Filter by price range (assuming the format is "min-max")
    if price_range:
        try:
            min_price, max_price = map(float, price_range.split('-'))
            car_listing = car_listing.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            pass  # Handle invalid price range input

    return render(request, 'home.html', {'car_listings': car_listing, 'query': query, 'price_range': price_range})
                  

def listedcars(request):
    '''list of cars'''
    return render(request, 'cars.html')

def services(request):
    '''services page'''
    return render(request, 'services.html')

def blogs(request):
    '''blogs page'''
    return render(request, 'blogs.html')

def autostores(request):
    '''auto stores page'''
    return render(request, 'store.html')

def about(request):
    '''about page'''
    return render(request, 'about.html')

def contact(request):
    '''contact page'''
    return render(request, 'contact.html')



