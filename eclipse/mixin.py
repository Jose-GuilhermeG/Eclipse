from django.views.generic import TemplateView

class paginas:
    def __init__(self,model,atual,quantia_por_pagina):
        self.model = model
        self.atual = atual
        self.quantia_por_pagina = quantia_por_pagina
        self.tamanho_model = len(model.objects.all())
        
    def has_next(self):
        if (self.atual * self.quantia_por_pagina) <= self.tamanho_model:
            return True
        return False
    
    def next_page_number(self):
        return self.atual + 1
    

class MultiItensView:
    def __init__(self,**kwargs):
        atributos = ['model','pages_name','paginate_by','context_object_name']
        self.valores_atributos = {}
        for atributo in atributos:
            self.valores_atributos[atributo] = getattr(self, atributo,'')
            
        return super().__init__()
    
    def get(self,request,*args,**kwargs):    
        return super().get(request,*args,**kwargs)

    def get_pages(self,*args,**kwargs):
        valor = self.request.GET.get(self.valores_atributos['pages_name'],1)
        if str(valor).isnumeric() and int(valor) > 1:
            return int(valor)
        return 1
    
    def get_query(self,quantia):
        return self.valores_atributos['model'].objects.all()[:quantia]
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        #itens query
        number_query = self.get_pages() * self.valores_atributos['paginate_by']
        itens = self.get_query(number_query)
        
        #page
        pagina_atual = self.get_pages()
        pagina_obj = paginas(self.valores_atributos['model'],pagina_atual,self.valores_atributos['paginate_by'])
        
        context[self.valores_atributos['context_object_name']] = itens
        context['pagina_obj'] = pagina_obj
        return context