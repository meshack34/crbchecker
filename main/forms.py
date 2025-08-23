from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class RegisterForm(UserCreationForm):
    terms = forms.BooleanField(
        required=True,
        label="I agree to the Terms of Service and Privacy Policy"
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name", "last_name", "surname",
            "phone", "id_number", "email",
            "password1", "password2"
        ]
        
        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Last Name"
            }),
            "surname": forms.TextInput(attrs={
                "placeholder": "Surname"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "e.g., +254712345678"
            }),
            "id_number": forms.TextInput(attrs={
                "placeholder": "Enter your 8-digit ID number"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email address"
            }),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove default labels from UserCreationForm fields
        for field in self.fields.values():
            field.label = ""
        # Set placeholders for password fields
        self.fields["password1"].widget.attrs["placeholder"] = "Create a password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm your password"


    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.surname = self.cleaned_data.get("surname")
        user.phone = self.cleaned_data["phone"]
        user.id_number = self.cleaned_data["id_number"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user





from django import forms
from .models import ReportPurpose

class ReportPurposeForm(forms.ModelForm):
    class Meta:
        model = ReportPurpose
        fields = ["purpose"]
        widgets = {
            "purpose": forms.RadioSelect(
                attrs={"class": "purpose-option"}
            )
        }
