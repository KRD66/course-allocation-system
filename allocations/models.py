# In allocations/models.py

from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)  # e.g., CS, MATH

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)  # e.g., CS101
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='teaching_courses')
    capacity = models.PositiveIntegerField()
    enrolled_count = models.PositiveIntegerField(default=0)
    schedule = models.CharField(max_length=200, blank=True)  # e.g., Mon/Wed 10-12
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)

    def available_slots(self):
        return self.capacity - self.enrolled_count

    def __str__(self):
        return f"{self.code} - {self.title}"

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('waitlisted', 'Waitlisted'), ('rejected', 'Rejected')],
        default='pending'
    )
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course')