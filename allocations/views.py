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
            print("=== REGISTRATION SUCCESS ===")
            print("Username:", user.username)
            print("Full Name:", user.full_name)
            print("Role:", user.role)
            print("Is Active:", user.is_active)
            print("Is Authenticated:", user.is_authenticated)
            print("Password hashed correctly?", user.check_password(form.cleaned_data['password1']))
            
            login(request, user)
            print("After login - request.user:", request.user)
            print("Is authenticated now?", request.user.is_authenticated)
            
            messages.success(request, f"Welcome, {user.full_name or user.username}!")
            return redirect('dashboard')
        else:
            print("Form errors:", form.errors)
    else:
        form = RegistrationForm()
    
    return render(request, 'allocations/register.html', {'form': form})

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'allocations/login.html'

    def get_success_url(self):
        # Redirect based on user role
        user = self.request.user
        if user.role == 'student':
            return reverse_lazy('dashboard')
        elif user.role == 'lecturer':
            return reverse_lazy('dashboard')  # We'll make lecturer dashboard later
        elif user.role == 'admin':
            return '/admin/'
        return reverse_lazy('home')
    
    
    
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Enrollment

@login_required
def dashboard(request):
    if request.user.role == 'student':
        # Student dashboard
        courses = Course.objects.all()
        my_enrollments = Enrollment.objects.filter(student=request.user).order_by('-requested_at')
        return render(request, 'allocations/student_dashboard.html', {
            'courses': courses,
            'my_enrollments': my_enrollments,
        })
    elif request.user.role == 'lecturer':
        my_courses = Course.objects.filter(lecturer=request.user)
        return render(request, 'allocations/lecturer_dashboard.html', {
            'my_courses': my_courses,
        })
    elif request.user.role == 'admin':
        return redirect('admin:index')
    else:
        messages.error(request, "Invalid user role.")
        return redirect('home')
    
    
@login_required
def submit_preferences(request):
    if request.user.role != 'student':
        messages.error(request, "Access denied.")
        return redirect('dashboard')
    
    courses = Course.objects.all()
    # In future: load saved preferences if any
    context = {
        'courses': courses,
        'page_title': 'Submit Course Preferences',
    }
    return render(request, 'allocations/submit_preferences.html', context)


@login_required
def view_timetable(request):
    if request.user.role != 'student':
        messages.error(request, "Access denied.")
        return redirect('dashboard')
    
    # Get only approved enrollments (real allocated courses)
    my_courses = Enrollment.objects.filter(
        student=request.user,
        status='approved'
    ).select_related('course')
    
    context = {
        'my_courses': my_courses,
        'page_title': 'My Timetable',
    }
    return render(request, 'allocations/view_timetable.html', context)


@login_required
def announcements(request):
    if request.user.role != 'student':
        messages.error(request, "Access denied.")
        return redirect('dashboard')
    
    # Placeholder announcements
    announcements_list = [
        {'title': 'Allocation Run Scheduled', 'date': 'Dec 10, 2025', 'body': 'The next allocation run is scheduled for December 20th.'},
        {'title': 'Preference Deadline Extended', 'date': 'Dec 5, 2025', 'body': 'Preference submission deadline extended to December 18th.'},
    ]
    context = {
        'announcements': announcements_list,
        'page_title': 'Announcements',
    }
    return render(request, 'allocations/announcements.html', context)

@login_required
def profile_settings(request):
    if request.method == 'POST':
        user = request.user
        user.full_name = request.POST.get('full_name', user.full_name)
        user.email = request.POST.get('email', user.email)
        if request.POST.get('new_password'):
            user.set_password(request.POST.get('new_password'))
        user.save()
        messages.success(request, "Profile updated successfully!")
    
    context = {
        'page_title': 'Profile Settings',
    }
    return render(request, 'allocations/profile_settings.html', context)    
    
    
    
    
    
    
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')