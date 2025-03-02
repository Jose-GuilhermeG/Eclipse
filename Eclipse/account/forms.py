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

class EndereçoForms(forms.Form):
    def __init__(self, *args, **kwargs):
        super(EndereçoForms,self).__init__(*args,**kwargs)
        self.fields['Cep'].label = ''
        self.fields['Cidade'].label = ''
        self.fields['Rua'].label = ''
        self.fields['Endereço'].label = ''
        self.fields['Complemento'].label = ''
        self.fields['Referencia'].label = ''
        self.fields['Telefone'].label = ''
                
            
    Cep = forms.CharField(max_length=9,widget=forms.TextInput(attrs={"placeholder":'Cep',"class": "input_form",}))
    Cidade = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Cidade","class": "input_form",}))
    Rua = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Rua',"class": "input_form",}))
    Endereço = forms.CharField(widget=forms.NumberInput(attrs={'placeholder' : 'Endereço',"class": "input_form",}))
    Complemento = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Complemento',"class": "input_form",}),required=False)
    Referencia = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Referencia',"class": "input_form",}),required=False)
    Telefone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder' : 'Telefone',"class": "input_form",}))
    
    def clean_Cep(self):
        data = self.cleaned_data["Cep"]
        data_format = data.split('-')
        data_string = ''
        for item in data_format:
            if item != '-':
                data_string += item
        return data_string
    