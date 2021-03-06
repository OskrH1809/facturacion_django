from hashlib import new
import json
from select import select
from typing import List
from urllib import response
from django import views
from django.http import JsonResponse
from django.views import View
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Cliente, Categoria, Detalle, Factura, Producto

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
                datos={'message':'Success','categoria':Categorias}
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
          

            # productos= list(Producto.objects.all().values())
            
            productox = list(Producto.objects.values('id','nombreProducto', 'precio', 'stock','categoria__nombreCategoria'))
                        
            if len(productox):
                datos={'message':'Success','Productos':productox}
            else:
                datos={'message':'Datos no encontrados'}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Producto.objects.create(nombreProducto=jd['nombreProducto'],
                            precio=jd['precio'],
                            stock=jd['stock'],
                            categoria_id=jd['categoria_id'],
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
            productoId.categoria_id=jd['categoria_id']
            productoId.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Datos no encontrados'}
        return JsonResponse(datos)
    
    def delete(self, request,id):
        productoId = list(Producto.objects.filter(id=id).values())
        if len(productoId) > 0:
            Producto.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Producto no encontrado'}
        return JsonResponse(datos)
        

class FacturaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs):  
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            facturaid = list(Factura.objects.filter(id=id).values())
            if len(facturaid) > 0:
                datos={'message':'Success','Productos':facturaid}
            else:
                datos={'message':'factura no encontrada'}
            return JsonResponse(datos)
        else:
            facturas = list(Factura.objects.values('id','cliente_id','fechaFactura','cliente__nombreCliente'))
            if len(facturas):
                datos={'message':'Success','facturas':facturas}
            else:
                datos={'message':'Datos no encontrados'}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        newFactura = Factura.objects.create(cliente_id=jd['cliente_id'],
                            )
        newFactura.save()
       
        datos={'message': 'success','id':newFactura.pk} 
        return  JsonResponse(datos)

    def put(self, request,id):
        jd=json.loads(request.body)
        facturaId = list(Factura.objects.filter(id=id).values())
        if len(facturaId) > 0:
            facturaId = Factura.objects.get(id=id)
            facturaId.cliente_id=jd['cliente_id']
            facturaId.fechaFactura=jd['fechaFactura']
            facturaId.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request,id):
        facturaId = list(Factura.objects.filter(id=id).values())
        if len(facturaId) > 0:
            Factura.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Factura no encontrada'}
        return JsonResponse(datos)
    

class DetalleView(View):
     @method_decorator(csrf_exempt)
     def dispatch(self, request , *args, **kwargs):  
        return super().dispatch(request, *args, **kwargs)

     def get(self, request,id=0):
        if(id>0):
            detalleId = list(Detalle.objects.filter(id=id).values())
            if len(detalleId) > 0:
                datos={'message':'Success','Productos':detalleId}
            else:
                datos={'message':'Detalles no encontrados'}
            return JsonResponse(datos)
        else:
            detalle = list(Detalle.objects.values('id','factura_id','producto_id','cantidad','precio','producto__nombreProducto'))
            if len(detalle):
                datos={'message':'Success','Detalles':detalle}
            else:
                datos={'message':'Datos no encontrados'}
            return JsonResponse(datos)

     def post(self, request):
        jd=json.loads(request.body)
        Detalle.objects.create(factura_id=jd['factura_id'],
                            producto_id=jd['producto_id'],
                            cantidad=jd['cantidad'],
                            precio=jd['precio'],
                            )
        datos={'message':'success'} 
        return JsonResponse(datos)
    
     def put(self, request,id):
        jd=json.loads(request.body)
        detalleId = list(Detalle.objects.filter(id=id).values())
        if len(detalleId) > 0:
            detalleId = Detalle.objects.get(id=id)
            detalleId.factura_id=jd['factura_id']
            detalleId.producto_id=jd['producto_id']
            detalleId.cantidad=jd['cantidad']
            detalleId.precio=jd['precio']
            detalleId.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Datos no encontrados'}
        return JsonResponse(datos)
     
     def delete(self, request,id):
        detalleId = list(Detalle.objects.filter(id=id).values())
        if len(detalleId) > 0:
            Detalle.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Detalles no encontrados'}
        return JsonResponse(datos)
    