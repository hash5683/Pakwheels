from django.contrib import admin
from .models import CarListing, CarBrand, Contact

class CarListingAdmin(admin.ModelAdmin):
    """Admin interface options for CarListing model."""
    list_display = ('car_name', 'make', 'model_year', 'color', 'mileage', 'price', 'status', 'date_added')
    search_fields = ('car_name', 'make__name', 'color')  # Search through the related CarBrand model
    list_filter = ('make', 'model_year', 'status')  # Filters for make, model year, and status
    ordering = ('-date_added',)  # Orders by date_added in descending order

    def get_queryset(self, request):
        """Customize the queryset to display related car brands' names."""
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('make')  # Optimize queries by using select_related for 'make'
        return queryset


class CarBrandAdmin(admin.ModelAdmin):
    """Admin interface options for CarBrand model."""
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


class ContactAdmin(admin.ModelAdmin):
    """Admin interface options for Contact model."""
    list_display = ('phone_number',)
    search_fields = ('phone_number',)


# Register models with admin site
admin.site.register(CarListing, CarListingAdmin)
admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(Contact, ContactAdmin)
