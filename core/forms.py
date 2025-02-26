from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Interesses

# User = get_user_model()

class MyCustomSignupForm(SignupForm):
    nome = forms.CharField(max_length=20, label="nome")
    sobrenome = forms.CharField(max_length=20, label="sobrenome")
    data_nascimento = forms.DateField( label="data_nascimento")
    telefone = forms.CharField(max_length=30, label="telefone")
    CPF = forms.CharField(max_length=50, label="CPF")

    interesses = forms.ModelMultipleChoiceField(
        queryset=Interesses.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Selecione seus interesses"
    )

    def save(self, request):

        # Salva o usuário com os campos extras
        user = super().save(request)

        user.nome = self.cleaned_data["nome"]
        user.sobrenome = self.cleaned_data["sobrenome"]
        user.data_nascimento = self.cleaned_data["data_nascimento"]
        user.telefone = self.cleaned_data["telefone"]
        user.CPF = self.cleaned_data["CPF"]
        interesses_selecionados = self.cleaned_data["interesses"]
        user.interesses.set(interesses_selecionados)
    
        user.save()

        return user

