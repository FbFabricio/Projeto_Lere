from django import forms
from .models import Cliente

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu usuário',
            'class': 'form-control',  
        }),
        label='Usuário'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'class': 'form-control', 
        }),
        label='Senha'
    )

    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = ['nome', 'carro', 'placa', 'servicos', 'telefone']