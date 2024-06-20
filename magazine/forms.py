import re
from django.core.exceptions import ValidationError
from django import forms
from .models import *

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = (
            'name',
            'agent_firstname',
            'agent_name',
            'agent_patronymic',
            'agent_telephone',
            'address',
        )
    def clean_agent_telephone(self):
        agent_telephone = self.cleaned_data['agent_telephone']
        if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', agent_telephone):
            return agent_telephone
        raise ValidationError('Телефон не соответствует шаблону')


class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = (
            'date_supply',
            'supplier',
        )

class Pos_supplyForm(forms.ModelForm):
    class Meta:
        model = Pos_supply
        fields = (
            'product',
            'supply',
            'count',
        )
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (
            'name',
            'description',
        )
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
        )
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'FIO_customer',
            'delivery_address',
            'delivery_type',
            'date_finish'
        )
#________________________________________________________________
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control', })
    )
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control', })
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', })
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        min_length=2
    )
    password = forms.CharField(
        label='Ваш пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', })
    )