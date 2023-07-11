from django import forms

class form_usuario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    nombreEmpresa = forms.CharField(max_length=40)
    email = forms.EmailField()