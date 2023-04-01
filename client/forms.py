from django import forms
from client.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=100, widget=forms.PasswordInput, label=("Parolni takrorlang"))

    def clean_fields(self):
        if self.cleaned_data["confirm"] != self.cleaned_data["password"]:
            raise ValidationError("Parol bir xil bulishi kerak")
        return self.cleaned_data["confirm"]

    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {
            "username": ("Login"),
            "password": ("Parol")
        }

        help_texts = {
            "username": ("Username")
        }

        widgets = {
            "password": forms.PasswordInput
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label=("Login"), required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label=("Parol"), required=True)
