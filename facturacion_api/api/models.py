from django.db import models
from django.forms import CharField, DateField, EmailField


class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=50)
    apellidoCliente = models.CharField(max_length=50)
    direccionCliente = models.TextField(max_length=200)
    fechaNacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=11,null=True)
    correoElectronico = models.EmailField(max_length=254,blank=True)

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria,null=True,on_delete=models.CASCADE)
    
    


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente,null=True,on_delete=models.CASCADE)
    fechaFactura = models.DateField( auto_now_add=True)

class Detalle(models.Model):
    factura = models.ForeignKey(Factura, null=True, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, null=True,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    