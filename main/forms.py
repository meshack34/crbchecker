from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "surname", "phone", "id_number", "email", "password1", "password2"]

    terms = forms.BooleanField(required=True, label="I agree to the Terms of Service and Privacy Policy")
