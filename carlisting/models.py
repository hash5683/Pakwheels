import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

def get_carbrand():
    """Returns a dictionary of car brands."""
    return {i: i for i in settings.CAR_BRANDS}

def get_modelyear():
    """Returns a dictionary of model years."""
    return {i: i for i in settings.MODEL_YEARS}

class Carlisting(models.Model):
    """Car model to represent a car listing."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carname = models.CharField(max_length=255)
    make = models.CharField(max_length=9, choices=get_carbrand())
    modelyear = models.CharField(max_length=4, choices=get_modelyear())
    image = models.ImageField(upload_to='car_images/')
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # Example DurationField to track how long the listing has been active
    listing_duration = models.DurationField(default=datetime.timedelta(days=0))
    
    STATUS_CHOICES = [
        ('AVL', 'Available'),
        ('SOLD', 'Sold'),
        ('PEND', 'Pending'),
    ]
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='AVL')

    def __str__(self):
        return f"{self.make} {self.carname} ({self.modelyear})"

class Contact(models.Model):
    """Contact model to represent a contact."""
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"),
        help_text=_("Enter a valid phone number.")
    )
    
    def __str__(self):
        return str(self.phone_number)
