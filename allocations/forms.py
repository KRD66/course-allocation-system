from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
    ]
    
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect,
        initial='student'
    )
    full_name = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'role', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make fields look nice
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Full Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'name@university.edu'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password (min 8 characters)'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})