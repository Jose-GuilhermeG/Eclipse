#django imports
from django import forms
from django.forms import ValidationError

#forms
class UserMixin(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email",'class' : 'input'}))
    Senha = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Senha",'class' : 'input'}))
    
class LoginForm(UserMixin):
    def clean(self):
        email = self.cleaned_data["Email"]
        
        return super().clean()
    
class CadastrarForm(UserMixin):
    Nome = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nome",'class' : 'input'}))