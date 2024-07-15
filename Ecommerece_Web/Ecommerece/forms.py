from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product,Category


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image','category','title','description','price']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

