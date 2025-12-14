from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('preferences/', views.submit_preferences, name='submit_preferences'),  
    path('timetable/', views.view_timetable, name='view_timetable'),  
    path('announcements/', views.announcements, name='announcements'),  
    path('profile/', views.profile_settings, name='profile_settings'), 
    path('lecturer/preferences/', views.lecturer_preferences, name='lecturer_preferences'),
    path('lecturer/allocation/', views.lecturer_allocation, name='lecturer_allocation'),
    path('admin/allocation-run/', views.admin_allocation_run, name='admin_allocation_run'),
]
