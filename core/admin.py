from django.contrib import admin
from .models import Categoria, Marca, Tamanho, Cor, Produto, ProdutoAtributo, Banner

@admin.register(Banner)
class CatAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'img')

@admin.register(Categoria)
class CatAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagem')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagem')

@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cor')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'cor', 'tamanho', 'status', 'is_feat')
    list_editable = ('status', 'is_feat')



class ProdutoAtributoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'preco', 'cor', 'tamanho')

admin.site.register(ProdutoAtributo, ProdutoAtributoAdmin)