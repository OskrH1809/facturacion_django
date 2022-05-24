import json
from typing import List
from django import views
from django.http import JsonResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Cliente, Categoria, Producto

class ClienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs):  
        return super().dispatch(request, *args, **kwargs)


    def get(self, request,id=0):
        if(id>0):
            clientesId = list(Cliente.objects.filter(id=id).values())
            if len(clientesId) > 0:
                datos={'message':'Success','Clientes':clientesId[0]}
            else:
                datos={'message':'Cliente no encontrado'}
            return JsonResponse(datos)
        else:
            clientes= list(Cliente.objects.values())
            if len(clientes):
                datos={'message':'Success','Clientes':clientes}
            else:
                datos={'message':'Datos no encontrados'}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Cliente.objects.create(nombreCliente=jd['nombreCliente'],
                            apellidoCliente=jd['apellidoCliente'],
                            direccionCliente=jd['direccionCliente'],
                            fechaNacimiento=jd['fechaNacimiento'],
                            telefono=jd['telefono'],
                            correoElectronico=jd['correoElectronico'])
        datos={'message':'success'} 
        return JsonResponse(datos)


    def put(self, request,id):
        jd=json.loads(request.body)
        clientesId = list(Cliente.objects.filter(id=id).values())
        if len(clientesId) > 0:
            clienteUpdate = Cliente.objects.get(id=id)
            clienteUpdate.nombreCliente=jd['nombreCliente']
            clienteUpdate.apellidoCliente=jd['apellidoCliente']
            clienteUpdate.direccionCliente=jd['direccionCliente']
            clienteUpdate.fechaNacimiento=jd['fechaNacimiento']
            clienteUpdate.telefono=jd['telefono']
            clienteUpdate.correoElectronico=jd['correoElectronico']
            clienteUpdate.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Datos no encontrados'}
        return JsonResponse(datos)
            


    def delete(self, request,id):
        clientesId = list(Cliente.objects.filter(id=id).values())
        if len(clientesId) > 0:
            Cliente.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Cliente no encontrado'}
        return JsonResponse(datos)


class CategoriaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs):  
        return super().dispatch(request, *args, **kwargs)


    def get(self, request,id=0):
        if(id>0):
            CategoriaId = list(Categoria.objects.filter(id=id).values())
            if len(CategoriaId) > 0:
                datos={'message':'Success','Categoria':CategoriaId[0]}
            else:
                datos={'message':'Categoria no encontrada'}
            return JsonResponse(datos)
        else:
            Categorias= list(Categoria.objects.values())
            if len(Categorias):
                datos={'message':'Success','Clientes':Categorias}
            else:
                datos={'message':'Datos no encontrados'}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Categoria.objects.create(nombreCategoria=jd['nombreCategoria'],
                            descripcion=jd['descripcion'],
                            )
        datos={'message':'success'} 
        return JsonResponse(datos)

    def put(self, request,id):
        jd=json.loads(request.body)
        CategoriaId = list(Categoria.objects.filter(id=id).values())
        if len(CategoriaId) > 0:
            CategoriaId = Categoria.objects.get(id=id)
            CategoriaId.nombreCategoria=jd['nombreCategoria']
            CategoriaId.descripcion=jd['descripcion']
            CategoriaId.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request,id):
        categoriasId = list(Categoria.objects.filter(id=id).values())
        if len(categoriasId) > 0:
            Categoria.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Categoria no encontrada'}
        return JsonResponse(datos)



class ProductoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs):  
        return super().dispatch(request, *args, **kwargs)


    def get(self, request,id=0):
        if(id>0):
            productoId = list(Producto.objects.filter(id=id).values())
            if len(productoId) > 0:
                datos={'message':'Success','Productos':productoId}
            else:
                datos={'message':'Producto no encontrado'}
            return JsonResponse(datos)
        else:
            productos= list(Producto.objects.values())
            if len(productos):
                datos={'message':'Success','Productos':productos}
            else:
                datos={'message':'Datos no encontrados'}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Producto.objects.create(nombreProducto=jd['nombreProducto'],
                            precio=jd['precio'],
                            stock=jd['stock'],
                            categoriaId_id=jd['categoriaId_id'],
                            )
        datos={'message':'success'} 
        return JsonResponse(datos)

    def put(self, request,id):
        jd=json.loads(request.body)
        productoId = list(Producto.objects.filter(id=id).values())
        if len(productoId) > 0:
            productoId = Producto.objects.get(id=id)
            productoId.nombreProducto=jd['nombreProducto']
            productoId.precio=jd['precio']
            productoId.stock=jd['stock']
            productoId.categoriaId_id=jd['categoriaId_id']
            productoId.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Datos no encontrados'}
        return JsonResponse(datos)
