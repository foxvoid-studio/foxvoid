from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    """
    Custom styling for the Django login form to match Tailwind CSS.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'bg-gray-700 border border-gray-600 text-gray-100 sm:text-sm rounded-lg focus:ring-orange-500 focus:border-orange-500 block w-full p-2.5 placeholder-gray-400',
        'placeholder': _('username')
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-700 border border-gray-600 text-gray-100 sm:text-sm rounded-lg focus:ring-orange-500 focus:border-orange-500 block w-full p-2.5 placeholder-gray-400',
        'placeholder': '••••••••'
    }))