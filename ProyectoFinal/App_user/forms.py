from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name','last_name','email']
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre completo',
            'last_name': 'Nombre del negocio',
            'email' : 'email'
        }

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if User.objects.filter(last_name=last_name).exists():
            raise forms.ValidationError('Ese nombre de negocio ya está registrado.')
        return last_name


class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Primer nombre"}), label= "Nombre completo")
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Nombre del negocio"}), label="Nombre del negocio")
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        help_text = {k:"" for k in fields}