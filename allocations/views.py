from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistrationForm



from django.shortcuts import render

def home(request):
    return render(request, 'allocations/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, f"Welcome, {user.full_name or user.username}! Your account has been created.")
            return redirect('home')  # We'll create this soon
    else:
        form = RegistrationForm()
    
    return render(request, 'allocations/register.html', {'form': form})