from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=200, required=True)
    role = forms.ChoiceField(
        choices=[('student', 'Student'), ('lecturer', 'Lecturer')],
        widget=forms.RadioSelect,
        initial='student'
    )

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'role', 'password1', 'password2']  # ← username added

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Full Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'name@university.edu'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})