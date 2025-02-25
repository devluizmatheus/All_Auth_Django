from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class MyCustomSignupForm(SignupForm):
    nome = forms.CharField(max_length=20)
    sobrenome = forms.CharField(max_length=20)
    data_nascimento = forms.DateField('Data Nascimento')
    telefone = forms.CharField(max_length=30)
    CPF = forms.CharField(max_length=50)

    def save(self, request):
        return super().save(request)

