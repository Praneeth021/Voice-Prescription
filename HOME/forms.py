from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users,Doctor


class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=100),
    last_name=forms.CharField(max_length=100),
    email=forms.EmailField(),
    class Meta:
        model=Users
        fields=['first_name','last_name','email','username','password1','password2','age','gender']


class DoctorRegisterForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['Education','Specialization','AadharNo','License']

        