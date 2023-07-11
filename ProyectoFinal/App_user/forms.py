from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name','last_name','email']



        