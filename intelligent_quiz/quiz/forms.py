from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

# -------------------------
# 1. Registration form
# -------------------------
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")


# -------------------------
# 2. Profile Update Forms
# -------------------------
class UserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'preferences']
        widgets = {
            'preferences': forms.Textarea(
                attrs={
                    'rows': 3,
                    'cols': 30,
                    'placeholder': '{"theme":"dark", "notifications":true}'
                }
            )
        }

    def clean_preferences(self):
        prefs = self.cleaned_data.get('preferences')
        if prefs:
            import json
            try:
                json.loads(prefs)
            except json.JSONDecodeError:
                raise forms.ValidationError("Preferences must be valid JSON")
        return prefs
