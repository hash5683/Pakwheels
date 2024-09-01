from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook = models.URLField(max_length=100)
    google = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName