from django.urls import path
from .views import home, categoria, marca, produto, categoria_list, marca_list, product_detail



urlpatterns = [
    path('', home, name='home'),
    path('categoria', categoria, name='category-list'),
    path('marca', marca, name='marca-list'),
    path('produto', produto, name='product-list'),
    path('categoria-list/<int:cat_id>', categoria_list, name='category-product-list' ),
    path('marca-list/<int:cat_id>', marca_list, name='marca_product_list' ),
    path('product/<str:slug>/<int:id>', product_detail, name='product_detail'),

]


