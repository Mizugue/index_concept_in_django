from django.db import models
from django.utils.html import mark_safe




class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='categoria_img/')

    def __str__(self):
        return self.titulo

    def image_tag_path(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.imagem.url))


class Cor(models.Model):
    titulo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo


class Banner(models.Model):
    img = models.CharField(max_length=250)
    alt_text = models.CharField(max_length=300)

class Tamanho(models.Model):
    titulo = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo


class Marca(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='marca_img/')
    def __str__(self):
        return self.titulo



class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    descricao=models.TextField()
    imagem = models.ImageField(upload_to='produtos_img/')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE) #foreign-> se esse produto tiver 20 marcas e apagarmos ele, apaga tudo
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_feat = models.BooleanField(default=False)



    def __str__(self):
        return self.titulo

class ProdutoAtributo(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE) #foreign-> se esse produto tiver 20 marcas e apagarmos ele, apaga tudo
    preco = models.PositiveIntegerField()
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)


    def __str__(self):
        return self.produto.titulo

