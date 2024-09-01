'''importing django forms'''
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    '''signup form'''
    class Meta:
        '''class'''
        model = User 
        fields = ['username', 'password1', 'password2']