from django.shortcuts import render
from .models import Categoria, Marca, Produto, ProdutoAtributo

def home(request):
    data = Produto.objects.filter(is_feat=True).order_by('id')
    return render(request, 'index.html', {'data': data})

def categoria(request):
    data = Categoria.objects.all().order_by('id')
    return render(request, 'category_list.html', {'data': data})


def marca(request):
    data = Marca.objects.all().order_by('id')
    return render(request, 'marca_list.html', {'data':data})


def produto(request):
    data = Produto.objects.all().order_by('id')
    cats = Produto.objects.values('categoria__titulo', 'categoria__id').distinct()
    marcas = Produto.objects.values('marca__titulo', 'marca__id').distinct()
    cores = Produto.objects.values('cor__titulo', 'cor__id').distinct()
    tamanhos = ProdutoAtributo.objects.values('tamanho__titulo', 'tamanho__id').distinct()

    return render(request, 'product_list.html',{'data': data, 'cats': cats, 'marcas': marcas, 'cores': cores, 'tamanhos': tamanhos})

def categoria_list(request, cat_id):
    categoria = Categoria.objects.get(id=cat_id)
    data = Produto.objects.filter(categoria=categoria).order_by('id')
    cats = Produto.objects.values('categoria__titulo', 'categoria__id').distinct()
    marcas = Produto.objects.values('marca__titulo', 'marca__id').distinct()
    cores = Produto.objects.values('cor__titulo', 'cor__id').distinct()
    tamanhos = ProdutoAtributo.objects.values('tamanho__titulo', 'tamanho__id').distinct()

    return render(request, 'category_product_list.html',{'data': data, 'cats': cats, 'marcas': marcas, 'cores': cores, 'tamanhos': tamanhos})


def marca_list(request, marca_id):
    marca = Categoria.objects.get(id=marca_id)
    data = Produto.objects.filter(categoria=categoria).order_by('id')
    cats = Produto.objects.values('categoria__titulo', 'categoria__id').distinct()
    marcas = Produto.objects.values('marca__titulo', 'marca__id').distinct()
    cores = Produto.objects.values('cor__titulo', 'cor__id').distinct()
    tamanhos = ProdutoAtributo.objects.values('tamanho__titulo', 'tamanho__id').distinct()

    return render(request, 'marca_product_list.html',{'data': data, 'cats': cats, 'marcas': marcas, 'cores': cores, 'tamanhos': tamanhos})

def marca_list(request, marca_id):
    marca = Categoria.objects.get(id=marca_id)
    data = Produto.objects.filter(categoria=categoria).order_by('id')
    cats = Produto.objects.values('categoria__titulo', 'categoria__id').distinct()
    marcas = Produto.objects.values('marca__titulo', 'marca__id').distinct()
    cores = Produto.objects.values('cor__titulo', 'cor__id').distinct()
    tamanhos = ProdutoAtributo.objects.values('tamanho__titulo', 'tamanho__id').distinct()

    return render(request, 'marca_product_list.html',{'data': data, 'cats': cats, 'marcas': marcas, 'cores': cores, 'tamanhos': tamanhos})

def product_detail(request,slug,id):
    product = Produto.objects.get(id=id)
    return render(request, 'product_detail.html', {'data':product})