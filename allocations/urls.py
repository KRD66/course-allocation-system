from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
]