from django.contrib import admin
from .models import Carlisting, Contact

class CarlistingAdmin(admin.ModelAdmin):
    list_display = ('carname', 'make', 'modelyear', 'color', 'mileage', 'price', 'status', 'date_added')
    search_fields = ('carname', 'make', 'color')
    list_filter = ('make', 'modelyear', 'status')
    ordering = ('-date_added',)  # Orders by date_added in descending order
    date_hierarchy = 'date_added'  # Adds a date navigation drill-down

class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
    search_fields = ('phone_number',)

admin.site.register(Carlisting, CarlistingAdmin)
admin.site.register(Contact, ContactAdmin)
