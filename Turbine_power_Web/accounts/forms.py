from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(label='email', required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  }))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password',
                                                                  'class': 'form-control',
                                                                  }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_password2(self):
        """Check if the two password entries match"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'username',
                                                             'class': 'form-control',
                                                             }))

    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Hasło',
                                                                 'class': 'form-control',
                                                                 }))

    class Meta:
        model = User
        fields = ['username', 'password']

