"""SegundaAtividade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SegundaAtividade.views import cliente,produto,home,pedido,categoria, fornecedor,funcionario,compra,endereco,usuario,pagamento,itenspedidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes', cliente.home, name="cliente.home"),
    path('clientes/insert', cliente.insert, name="cliente.insert"),
    path('clientes/edit/<id>', cliente.edit, name="cliente.edit"),
    path('clientes/delete/<id>', cliente.delete, name="cliente.delete"),
    
    path('produto', produto.home, name="produto.home"),
    path('produto/insert', produto.insert, name="produto.insert"),
    path('produto/edit/<id>\<nome>', produto.edit, name="produto.edit"),
    path('produto/delete/<id>', produto.delete, name="produto.delete"),
    
    path('pedido', pedido.home, name="pedido.home"),
    path('pedido/insert', pedido.insert, name="pedido.insert"),
    path('pedido/edit/<id>', pedido.edit, name="pedido.edit"),
    path('pedido/delete/<id>', pedido.delete, name="pedido.delete"),
    
    path('categoria', categoria.home, name="categoria.home"),
    path('categoria/insert', categoria.insert, name="categoria.insert"),
    path('categoria/edit/<id>\<nome>', categoria.edit, name="categoria.edit"),
    path('categoria/delete/<id>', categoria.delete, name="categoria.delete"),
    
    path('fornecedor', fornecedor.home, name="fornecedor.home"),
    path('fornecedor/insert', fornecedor.insert, name="fornecedor.insert"),
    path('fornecedor/edit/<id>\<nome>', fornecedor.edit, name="fornecedor.edit"),
    path('fornecedor/delete/<id>', fornecedor.delete, name="fornecedor.delete"),
    
    path('funcionario', funcionario.home, name="funcionario.home"),
    path('funcionario/insert', funcionario.insert, name="funcionario.insert"),
    path('funcionario/edit/<id>\<nome>', funcionario.edit, name="funcionario.edit"),
    path('funcionario/delete/<id>', funcionario.delete, name="funcionario.delete"),

    path('usuario', usuario.home, name="usuario.home"),
    path('usuario/insert', usuario.insert, name="usuario.insert"),
    path('usuario/edit/<id>', usuario.edit, name="usuario.edit"),
    path('usuario/delete/<id>', usuario.delete, name="usuario.delete"),

    path('endereco', endereco.home, name="endereco.home"),
    path('endereco/insert', endereco.insert, name="endereco.insert"),
    path('endereco/edit/<id>', endereco.edit, name="endereco.edit"),
    path('endereco/delete/<id>', endereco.delete, name="endereco.delete"),

    path('pagamento', pagamento.home, name="pagamento.home"),
    path('pagamento/insert', pagamento.insert, name="pagamento.insert"),
    path('pagamento/edit/<id>\<nome>', pagamento.edit, name="pagamento.edit"),
    path('pagamento/delete/<id>', pagamento.delete, name="pagamento.delete"),

    path('compra', compra.home, name="compra.home"),
    path('compra/insert', compra.insert, name="compra.insert"),
    path('compra/edit/<id>', compra.edit, name="compra.edit"),
    path('compra/delete/<id>', compra.delete, name="compra.delete"),

    path('itenspedidos', itenspedidos.home, name="itenspedidos.home"),
    path('itenspedidos/insert', itenspedidos.insert, name="itenspedidos.insert"),
    path('itenspedidos/edit/<id>', itenspedidos.edit, name="itenspedidos.edit"),
    path('itenspedidos/delete/<id>', itenspedidos.delete, name="itenspedidos.delete"),

    path('', home.home, name="home")
]
