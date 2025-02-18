from django import forms

class ProdutoPromoçãoForm(forms.ModelForm):
    Desconto = forms.IntegerField(max_value=100)
    Acaba = forms.TimeField()
    
