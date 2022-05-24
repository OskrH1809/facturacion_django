from django.urls import path

from .views import CategoriaView, ClienteView, ProductoView, FacturaView

urlpatterns = [
    #cliente 
    path('cliente',ClienteView.as_view(),name='cliente_lista'),
    path('cliente/<int:id>',ClienteView.as_view(),name='cliente_procesos'),

    # categoria
    path('categoria',CategoriaView.as_view(),name='categoria_lista'),
    path('categoria/<int:id>',CategoriaView.as_view(),name='categoria_procesos'),

    # producto
    path('producto', ProductoView.as_view(),name='producto_lista'),
    path('producto/<int:id>',ProductoView.as_view(),name='producto_procesos'),

    # factura
    path('factura', FacturaView.as_view(),name='factura_lista'),
    path('factura/<int:id>',FacturaView.as_view(),name='factura_procesos'),

    
]