from django.contrib import admin

# Register your models here.

from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id','nome')
    # list_filter = ('categoria','nome','sobrenome',)
    search_fields = ('nome','sobrenome','telefone','email','descricao','categoria__nome')
    list_per_page = 10
    list_editable = ('telefone','mostrar')
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
