from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    company = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=100, required=False)
    zip_code = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=100, required=False)
    avatar = forms.ImageField(required=False)
    phone = forms.CharField(max_length=100, required=False)
