import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

def get_model_years():
    """Returns a list of tuples representing car model years from 1970 to the current year."""
    current_year = datetime.datetime.now().year
    return [(str(year), str(year)) for year in range(1970, current_year + 1)]


class CarBrand(models.Model):
    """Model representing a car brand."""
    code = models.CharField(max_length=5, unique=True)  # Short code like 'TOY'
    name = models.CharField(max_length=255, unique=True)  # Full name like 'Toyota'

    def __str__(self):
        """Return a string representation of the car brand."""
        return self.name


class CarListing(models.Model):
    """Model representing a car listing."""

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='car_listings')
    car_name = models.CharField(max_length=255)
    make = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model_year = models.CharField(max_length=4, choices=get_model_years())
    image = models.ImageField(upload_to='car_images/')
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    listing_duration = models.DurationField(default=datetime.timedelta(days=0))

    STATUS_CHOICES = [
        ('AVL', 'Available'),
        ('SOLD', 'Sold'),
        ('PEND', 'Pending'),
    ]
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='AVL')

    def __str__(self):
        """Return a string representation of the car listing."""
        return f"{self.make} {self.car_name} ({self.model_year})"


class Contact(models.Model):
    """Model representing a contact with a phone number."""

    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"),
        help_text=_("Enter a valid phone number.")
    )

    def __str__(self):
        """Return the phone number as a string."""
        return str(self.phone_number)
