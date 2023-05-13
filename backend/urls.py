from django.urls import path
from .views import GuiadespachoView,EstadoVentaView, VentaView, DireccionView, ProductoView, SucursalView, EmpleadoView, GeneroView, ConsolaView, RolView, ComunaView, ClienteView, BodegaView, Detalle_bodegaView, RegionView, DetalleVentaView, MetodoPagoView

urlpatterns = [
    path('direcciones/', DireccionView.as_view(), name='lista_direcciones'),
    path('direcciones/<int:id>', DireccionView.as_view(), name='proceso_direcciones'),
    path('productos/', ProductoView.as_view(), name='lista_productos'),
    path('productos/<int:id>', ProductoView.as_view(), name='proceso_productos'),
    path('sucursales/', SucursalView.as_view(), name='sucursales'),
    path('sucursales/<int:id>', SucursalView.as_view(), name='proceso_sucursales'),
    path('empleados/', EmpleadoView.as_view(), name='empleados'),
    path('empleados/<int:id>', EmpleadoView.as_view(), name='proceso_empleados'),
    path('generos/', GeneroView.as_view(), name='generos'),
    path('generos/<int:id>', GeneroView.as_view(), name='proceso_generos'),
    path('consolas/', ConsolaView.as_view(), name='consolas'),
    path('consolas/<int:id>', ConsolaView.as_view(), name='proceso_consolas'),
    path('roles/', RolView.as_view(), name='roles'),
    path('roles/<int:id>', RolView.as_view(), name='proceso_roles'),
    path('comunas/', ComunaView.as_view(), name='comunas'),
    path('comunas/<int:id>', ComunaView.as_view(), name='proceso_comunas'),
    path('clientes/', ClienteView.as_view(), name='clientes'),
    path('clientes/<int:id>', ClienteView.as_view(), name='proceso_clientes'),
    path('detalleVentas/', DetalleVentaView.as_view(), name='detalleVenta'),
    path('detalleVentas/<int:id>', DetalleVentaView.as_view(), name='proceso_detalleVenta'),
    path('metodoPagos/', MetodoPagoView.as_view(), name='metodopago'),
    path('metodoPagos/<int:id>',MetodoPagoView.as_view(), name='proceso_metodopago'),

    path('bodegas/', BodegaView.as_view(), name='bodegas'),
    path('bodegas/<int:id>', BodegaView.as_view(), name='proceso_bodegas'),
    path('detalleBodegas/', Detalle_bodegaView.as_view(), name='detallebodegas'),
    path('detalleBodegas/<int:id>', Detalle_bodegaView.as_view(), name='proceso_detallebodegas'),
    path('regiones/', RegionView.as_view(), name='region'),
    path('regiones/<int:id>', RegionView.as_view(), name='proceso_region'),


    path('ventas/', VentaView.as_view(), name='ventas'),
    path('ventas/<int:id>', VentaView.as_view(), name='ventasporid'),
    path('estadoVentas/', EstadoVentaView.as_view(), name='Estado_Venta'),
    path('estadoVentas/<int:id>', EstadoVentaView.as_view(), name='estadoventaporid'),
    path('guiasDespacho', GuiadespachoView.as_view(), name='Guia_despacho'),
    path('guiasDespacho/<int:id>', GuiadespachoView.as_view(), name='Guia_despacho'),

]




