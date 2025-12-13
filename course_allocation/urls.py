from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allocations.urls')),                    # ← our app URLs
    path('accounts/', include('django.contrib.auth.urls')),   # ← login, logout, etc.
]