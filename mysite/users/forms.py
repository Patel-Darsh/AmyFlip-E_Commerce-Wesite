from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from django.core.exceptions import ValidationError


#----------------------------- Sign Up Form -----------------------------------------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:                     #contains data of the form 
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if any(char.isdigit() for char in data):
            raise ValidationError("First name cannot contain numbers.")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if any(char.isdigit() for char in data):
            raise ValidationError("Last name cannot contain numbers.")
        return data
    
class ProfFormCreating(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'location', 'user_type']

    

class ProfFormEditing(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'location', 'user_type']