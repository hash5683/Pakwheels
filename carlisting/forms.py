from django import forms
from .models import Carlisting

class CarForm(forms.ModelForm):
    class Meta:
        model = Carlisting
        fields = ['carname', 'make', 'modelyear', 'image', 'color', 'mileage', 'price', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }