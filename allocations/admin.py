from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Course, Enrollment

# Custom User admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'full_name', 'email', 'role', 'is_staff')
    list_filter = ('role',)
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('full_name', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('full_name', 'role')}),
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('name', 'code')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'department', 'lecturer', 'capacity', 'enrolled_count', 'available_slots')
    list_filter = ('department',)
    search_fields = ('code', 'title')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'requested_at')
    list_filter = ('status', 'course__department')
    search_fields = ('student__username', 'course__code')