from django.contrib import admin
from .models import Cliente,Categoria,Producto,Factura,Detalle
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(Detalle)

