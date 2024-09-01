'''importing the shortcuts and form'''
from django.shortcuts import render, redirect
from .forms import SignupForm

# signup page
def user_signup(request):
    '''signup page'''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
