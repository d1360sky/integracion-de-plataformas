from django.shortcuts import render
from django.views import View
from .models import Producto, Direccion, Sucursal, Empleado, Genero, Consola, Rol, Comuna, Cliente, Bodega, Detalle_bodega, Region, DetalleVenta, MetodoPago,Venta,EstadoVenta
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import requests

##ValorUF##
urlApiUf = "https://mindicador.cl/api/uf"
response = requests.get(urlApiUf)
data=response.json()
valorUf = data['serie'][0]['valor']

#### Crud Direciones ##########
class DireccionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            direcciones=list(Direccion.objects.filter(idDireccion=id).values())
            if len(direcciones)>0:
                direccion=direcciones[0]
                datos={'message':"Success", 'direcciones': direccion}
            else:
                datos={'message': "Direcciones no encontradas..."}
            return JsonResponse(datos)
        else:
            direcciones = list(Direccion.objects.values())
            if len(direcciones)>0:
                datos={'message':"Success", 'direcciones': direcciones}
            else:
                datos={'message': "Direcciones no encontradas..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Direccion.objects.create(nombreCalle=jd['nombreCalle'], numeroCasa=jd['numeroCasa'],comuna_id=jd['comuna_id'])
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        direcciones=list(Direccion.objects.filter(idDireccion=id).values())
        if len(direcciones)>0:
            direccion=Direccion.objects.get(idDireccion=id)
            direccion.nombreCalle=jd['nombreCalle']
            direccion.numeroCasa=jd['numeroCasa']
            direccion.comuna_id=jd['comuna_id']
            direccion.save()
            datos = {'message': "succes"}
        else: 
            datos={'message': "Direcciones no encontradas..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        direcciones = list(Direccion.objects.filter(idDireccion=id).values())
        if len(direcciones)>0:
            Direccion.objects.filter(idDireccion=id).delete()
            datos = {'message': "succes"}

        else:
            datos={'message': "Direcciones no encontradas..."}
        return JsonResponse(datos)
    




### CRUD PRODUCTO ###

class ProductoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            productos=list(Direccion.objects.filter(idProducto=id).values())
            if len(productos)>0:
                producto=productos[0]
                datos={'message':"Correcto", 'productos': producto}
            else:
                datos={'message': "Prodcutos no encontrados..."}
            return JsonResponse(datos)
        else:
            productos = list(Producto.objects.values())
            if len(productos)>0:
                datos={'message':"Correcto", 'productos': productos}
            else:
                datos={'message': "Productos no encontrados..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Producto.objects.create(
            nombreProducto=jd['nombreProducto'],
            descripcion=jd['descripcion'],
            precio=jd['precio'],
            stock=jd['stock'],
            imagen=jd['imagen'],
            genero_id=jd['genero_id'],
            consola_id=jd['consola_id']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        productos=list(Producto.objects.filter(idProducto=id).values())
        if len(productos)>0:
            producto=Producto.objects.get(idProducto=id)
            producto.nombreProducto=jd['nombreProducto']
            producto.descripcion=jd['descripcion']
            producto.precio=jd['precio']
            producto.imagen=jd['imagen']
            producto.genero_id=jd['genero_id']
            producto.consola_id=jd['consola_id']
            producto.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Productos no encontradas..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        productos = list(Producto.objects.filter(idProducto=id).values())
        if len(productos)>0:
            Producto.objects.filter(idProducto=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Productos no encontrados..."}
        return JsonResponse(datos)


## CRUD SUCURSAL ##

class SucursalView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            sucursales=list(Sucursal.objects.filter(idSucursal=id).values())
            if len(sucursales)>0:
                sucursal=sucursales[0]
                datos={'message':"Correcto", 'sucursales': sucursal}
            else:
                datos={'message': "Sucursales no encontradas..."}
            return JsonResponse(datos)
        else:
            sucursales = list(Sucursal.objects.values())
            if len(sucursales)>0:
                datos={'message':"Correcto", 'sucursales': sucursales}
            else:
                datos={'message': "Sucursales no encontradas..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Sucursal.objects.create(
            direccion_id=jd['direccion_id']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        sucursales=list(Sucursal.objects.filter(idSucursal=id).values())
        if len(sucursales)>0:
            sucursal=Sucursal.objects.get(idSucursal=id)
            sucursal.direccion_id=jd['direccion_id']
            sucursal.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Sucursales no encontradas..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        sucursales = list(Sucursal.objects.filter(idSucursal=id).values())
        if len(sucursales)>0:
            Sucursal.objects.filter(idSucursal=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Sucursales no encontrados..."}
        return JsonResponse(datos)
    

## EMPLEADO ##
class EmpleadoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            empleados=list(Empleado.objects.filter(idEmpleado=id).values())
            if len(empleados)>0:
                empleado=empleados[0]
                datos={'message':"Correcto", 'empleado': empleado}
            else:
                datos={'message': "Empleados no encontrados..."}
            return JsonResponse(datos)
        else:
            empleados = list(Empleado.objects.values())
            if len(empleados)>0:
                datos={'message':"Correcto", 'Empleados': empleados}
            else:
                datos={'message': "Empleados no encontrados..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Empleado.objects.create(
            nombreEmpleado=jd['nombreEmpleado'],
            rol_id=jd['rol_id']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        empleados=list(Empleado.objects.filter(idEmpleado=id).values())
        if len(empleados)>0:
            empleado=Empleado.objects.get(idEmpleado=id)
            empleado.nombreEmpleado=jd['nombreEmpleado']
            empleado.rol_id=jd['rol_id']
            empleado.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Empleados no encontradas..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        empleados = list(Empleado.objects.filter(idEmpleado=id).values())
        if len(empleados)>0:
            Empleado.objects.filter(idEmpleado=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Empleados no encontrados..."}
        return JsonResponse(datos)


## GENEROS ##
class GeneroView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            generos=list(Genero.objects.filter(idGenero=id).values())
            if len(generos)>0:
                genero=generos[0]
                datos={'message':"Correcto", 'genero': genero}
            else:
                datos={'message': "Generos no encontrados..."}
            return JsonResponse(datos)
        else:
            generos = list(Genero.objects.values())
            if len(generos)>0:
                datos={'message':"Correcto", 'generos': generos}
            else:
                datos={'message': "Generos no encontrados..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Genero.objects.create(
            nombreGenero=jd['nombreGenero']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        generos=list(Genero.objects.filter(idGenero=id).values())
        if len(generos)>0:
            genero=Genero.objects.get(idGenero=id)
            genero.nombreGenero=jd['nombreGenero']
            genero.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Genero no encontradas..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        generos = list(Genero.objects.filter(idGenero=id).values())
        if len(generos)>0:
            Genero.objects.filter(idGenero=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Genero no encontrado..."}
        return JsonResponse(datos)
    
##CONSOLA##
class ConsolaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            consolas=list(Consola.objects.filter(idConsola=id).values())
            if len(consolas)>0:
                consola=consolas[0]
                datos={'message':"Correcto", 'consola': consola}
            else:
                datos={'message': "Consolas no encontradas..."}
            return JsonResponse(datos)
        else:
            consolas = list(Consola.objects.values())
            if len(consolas)>0:
                datos={'message':"Correcto", 'consolas': consolas}
            else:
                datos={'message': "Consolas no encontradas..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Consola.objects.create(
            nombreConsola=jd['nombreConsola']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        consolas=list(Consola.objects.filter(idConsola=id).values())
        if len(consolas)>0:
            consola=Consola.objects.get(idConsola=id)
            consola.nombreConsola=jd['nombreConsola']
            consola.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Consola no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        consolas = list(Consola.objects.filter(idConsola=id).values())
        if len(consolas)>0:
            Consola.objects.filter(idConsola=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Consola no encontrada..."}
        return JsonResponse(datos)

##ROL##
class RolView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            roles=list(Rol.objects.filter(idRol=id).values())
            if len(roles)>0:
                rol=roles[0]
                datos={'message':"Correcto", 'rol': rol}
            else:
                datos={'message': "roles no encontrados..."}
            return JsonResponse(datos)
        else:
            roles = list(Rol.objects.values())
            if len(roles)>0:
                datos={'message':"Correcto", 'roles': roles}
            else:
                datos={'message': "roles no encontrados..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Rol.objects.create(
            nombreRol=jd['nombreRol']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        roles=list(Rol.objects.filter(idRol=id).values())
        if len(roles)>0:
            rol=Rol.objects.get(idRol=id)
            rol.nombreRol=jd['nombreRol']
            rol.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Rol no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        roles = list(Rol.objects.filter(idRol=id).values())
        if len(roles)>0:
            Rol.objects.filter(idRol=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Rol no encontrado..."}
        return JsonResponse(datos)

##COMUNA##
class ComunaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            comunas=list(Comuna.objects.filter(idComuna=id).values())
            if len(comunas)>0:
                comuna=comunas[0]
                datos={'message':"Correcto", 'comuna': comuna}
            else:
                datos={'message': "comuna no encontrada..."}
            return JsonResponse(datos)
        else:
            comunas = list(Comuna.objects.values())
            if len(comunas)>0:
                datos={'message':"Correcto", 'comunas': comunas}
            else:
                datos={'message': "comunas no encontradas..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Comuna.objects.create(
            nombreComuna=jd['nombreComuna']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        comunas=list(Comuna.objects.filter(idComuna=id).values())
        if len(comunas)>0:
            comuna=Comuna.objects.get(idComuna=id)
            comuna.nombreComuna=jd['nombreComuna']
            comuna.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Comuna no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        comunas = list(Comuna.objects.filter(idComuna=id).values())
        if len(comunas)>0:
            Comuna.objects.filter(idComuna=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Comuna no encontrada..."}
        return JsonResponse(datos)



#CLIENTE#
class ClienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
            if(id>0):
                clientes=list(Cliente.objects.filter(idCliente=id).values())
                if len(clientes)>0:
                    cliente=clientes[0]
                    datos={'message':"Success", 'direcciones': cliente}
                else:
                    datos={'message': "Direcciones no encontradas..."}
                return JsonResponse(datos)
            else:
                clientes = list(Cliente.objects.values())
                if len(clientes)>0:
                    datos={'message':"Success", 'direcciones': clientes}
                else:
                    datos={'message': "Direcciones no encontradas..."}
                return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Cliente.objects.create(
            nombreCliente=jd['nombreCliente'], nombreUsuario=jd['nombreUsuario'], telefono=jd['telefono'],
            contraseña=jd['contraseña'], correo=jd['correo'], direccion_id=jd['direccion_id']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        clientes=list(Cliente.objects.filter(idClinete=id).values())
        if len(clientes)>0:
            cliente=Cliente.objects.get(idCliente=id)
            cliente.nombreCliente=jd['nombreCliente']
            cliente.nombreUsuario=jd['nombreUsuario']
            cliente.telefono=jd['telefono']
            cliente.contraseña=jd['contraseña']
            cliente.correo=jd['correo']
            cliente.direccion=jd['direccion']
            cliente.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "cliente no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        clientes = list(Cliente.objects.filter(idClientes=id).values())
        if len(clientes)>0:
            Cliente.objects.filter(idCliente=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "cliente no encontrada..."}
        return JsonResponse(datos)

#DetalleVenta##############################################################################################################################################################
class DetalleVentaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if(id>0):
            detalleVentas=list(DetalleVenta.objects.filter(idDetalleVenta=id).values())
            if len(detalleVentas)>0:
                detalleVenta=detalleVentas[0]
                datos={'message':"Correcto", 'detalleVenta': detalleVenta}
            else:
                datos={'message': "Detalle Venta no encontrada... "}
            return JsonResponse(datos)
        else:
            detalleVentas = list(DetalleVenta.objects.values())
            if len(detalleVentas)>0:
                datos={'message':"Correcto", 'detalleVenta': detalleVentas}
            else:
                datos={'message': "Detalle venta no encontradas..."}
            return JsonResponse(datos)
    
    def post(self, request):
        data = json.loads(request.body)

                    


        for detalle_data in data:
            cantidad = detalle_data['cantidad']
            producto_id = detalle_data['producto_id']
            venta_id = detalle_data['venta_id']

            DetalleVenta.objects.create(
                cantidad=cantidad,
                producto_id=producto_id,
                venta_id=venta_id
            )
        
        datos = {'message': "Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        detalleVentas=list(DetalleVenta.objects.filter(idDetalleVenta=id).values())
        if len(detalleVentas)>0:
            detalleVenta=DetalleVenta.objects.get(idDetalleVenta=id)
            detalleVenta.producto_id=jd['producto_id']
            detalleVenta.cantidad=jd['cantidad']
            detalleVenta.fecha=jd['fecha']
            detalleVenta.venta_id=jd['venta_id']
            detalleVenta.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Detalle venta no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        detalleVentas = list(DetalleVenta.objects.filter(idDetalleVenta=id).values())
        if len(detalleVentas)>0:
            DetalleVenta.objects.filter(idDetalleVenta=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Detalle venta no encontrada..."}
        return JsonResponse(datos)

### Metodo Pago ###
class MetodoPagoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            metodopagos=list(MetodoPago.objects.filter(idMetodoPago=id).values())
            if len(metodopagos)>0:
                metodopago=metodopagos[0]
                datos={'message':"Correcto", 'metodoPago': metodopago}
            else:
                datos={'message': "metodo Pago no encontrado..."}
            return JsonResponse(datos)
        else:
            metodopagos = list(MetodoPago.objects.values())
            if len(metodopagos)>0:
                datos={'message':"Correcto", 'metodoPago': metodopagos}
            else:
                datos={'message': "metodoPago no encontradas..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        MetodoPago.objects.create(
            tipoMetodo=jd['tipoMetodo']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        metodopagos=list(MetodoPago.objects.filter(idMetodoPago=id).values())
        if len(metodopagos)>0:
            metodopago=MetodoPago.objects.get(idMetodoPago=id)
            metodopago.tipoMetodo=jd['tipoMetodo']
            metodopago.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "metodoPago no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        metodopagos = list(MetodoPago.objects.filter(idMetodoPagos=id).values())
        if len(metodopagos)>0:
            MetodoPago.objects.filter(idMetodoPago=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "metodoPago no encontrada..."}
        return JsonResponse(datos) 

####Crud Bodega####
class BodegaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            bodegas=list(Bodega.objects.filter(idBodega=id).values())
            if len(bodegas)>0:
                bodega=bodegas[0]
                datos={'message':"Correcto", 'bodega': bodega}
            else:
                datos={'message': "bodega no encontrada... "}
            return JsonResponse(datos)
        else:
            bodegas = list(Bodega.objects.values())
            if len(bodegas)>0:
                datos={'message':"Correcto", 'bodegas': bodegas}
            else:
                datos={'message': "bodegas no encontradas..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Bodega.objects.create(
            direccionbodega_id=jd['direccionbodega_id']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        bodegas=list(Bodega.objects.filter(idBodega=id).values())
        if len(bodegas)>0:
            bodega=Bodega.objects.get(idBodega=id)
            bodega.direccionbodega_id=jd['direccionbodega_id']
            bodega.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Bodega no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        bodegas = list(Bodega.objects.filter(idBodega=id).values())
        if len(bodegas)>0:
            Bodega.objects.filter(idBodega=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Bodega no encontrada..."}
        return JsonResponse(datos)

####CRUD detalleBodega##########################################################################################################################

class Detalle_bodegaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if(id>0):
            detalleBodegas=list(Detalle_bodega.objects.filter(idDetalleBodega=id).values())
            if len(detalleBodegas)>0:
                detalleBodega=detalleBodegas[0]
                datos={'message':"Correcto", 'Detallebodega': detalleBodega}
            else:
                datos={'message': "Detalle bodega no encontrada... "}
            return JsonResponse(datos)
        else:
            detalleBodegas = list(Detalle_bodega.objects.values())
            if len(detalleBodegas)>0:
                datos={'message':"Correcto", 'detalleBodega': detalleBodegas}
            else:
                datos={'message': "Detalle bodega no encontradas..."}
            return JsonResponse(datos)

    def post(self, request):
        data = json.loads(request.body)

        for detalle_data in data:
            bodegaa_id = detalle_data['bodegaa_id']
            cantidadProd = detalle_data['cantidadProd']
            ubicacion_producto_id = detalle_data['ubicacion_producto_id']
            producto_id = detalle_data['producto_id']

            Detalle_bodega.objects.create(
                bodegaa_id=bodegaa_id,
                cantidadProd=cantidadProd,
                ubicacion_producto_id=ubicacion_producto_id,
                producto_id=producto_id
            )

        datos={'message':"Correcto"}
        return JsonResponse(datos)

    

    def put(self, request, id):
        jd=json.loads(request.body)
        detalleBodegas=list(Detalle_bodega.objects.filter(idDetalleBodega=id).values())
        if len(detalleBodegas)>0:
            detalleBodega=Detalle_bodega.objects.get(idDetalleBodega=id)
            detalleBodega.bodegaa_id=jd['bodegaa_id']
            detalleBodega.cantidadProd=jd['cantidadProd']
            detalleBodega.lugarProd=jd['lugarProd']
            detalleBodega.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Detalle bodega no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        detalleBodegas = list(Detalle_bodega.objects.filter(idDetalleBodega=id).values())
        if len(detalleBodegas)>0:
            Detalle_bodega.objects.filter(idDetalleBodega=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Detalle bodega no encontrada..."}
        return JsonResponse(datos)

#####REGION######

class RegionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            regiones=list(Region.objects.filter(idRegion=id).values())
            if len(regiones)>0:
                region=regiones[0]
                datos={'message':"Correcto", 'region': region}
            else:
                datos={'message': "Region no encontrada... "}
            return JsonResponse(datos)
        else:
            regiones = list(Region.objects.values())
            if len(regiones)>0:
                datos={'message':"Correcto", 'Regiones': regiones}
            else:
                datos={'message': "Regiones no encontradas..."}
            return JsonResponse(datos)
        

    def post(self, request):
        jd = json.loads(request.body)
        Region.objects.create(
            nombreRegion=jd['nombreRegion']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        regiones=list(Region.objects.filter(idRegion=id).values())
        if len(regiones)>0:
            region=Region.objects.get(idRegion=id)
            region.nombreRegion=jd['nombreRegion']
            region.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Region no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        regiones = list(Region.objects.filter(idRegion=id).values())
        if len(regiones)>0:
            Region.objects.filter(idRegion=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Region no encontrada..."}
        return JsonResponse(datos)

##Venta##
class VentaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            ventas=list(Venta.objects.filter(idVenta=id).values())
            if len(ventas)>0:
                venta=ventas[0]
                datos={'message':"Correcto", 'bodega': venta}
            else:
                datos={'message': "Venta no encontrada... "}
            return JsonResponse(datos)
        else:
            ventas = list(Venta.objects.values())
            if len(ventas)>0:
                datos={'message':"Correcto", 'Ventas': ventas}
            else:
                datos={'message': "Venta no encontradas..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Venta.objects.create(
            totalPago=float(jd['totalPago'])/float(valorUf),
            cliente_id=jd['cliente_id'],
            metodoPago_id=jd['metodoPago_id'],
            estadoVenta_id=jd['estadoVenta_id']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
            jd=json.loads(request.body)
            Detalle=list(DetalleVenta.objects.filter(idDetalleVenta=id).values())
            if len(Detalle)>0:
                Detalle=DetalleVenta.objects.get(idDetalleVenta=id)
                Detalle.cantidad=jd['cantidad']
                Detalle.fecha=jd['fecha']
                Detalle.producto=jd['producto']
                Detalle.save()
                datos = {'message': "correcto"}
            else: 
                datos={'message': "Venta no encontrada..."}
            return JsonResponse(datos)

    def delete(self, request, id):
        Venta = list(Venta.objects.filter(idVenta=id).values())
        if len(Venta)>0:
            Venta.objects.filter(idVenta=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Venta no encontrada..."}
        return JsonResponse(datos)

##EstadoVenta##
class EstadoVentaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            estados=list(EstadoVenta.objects.filter(idEstadoVenta=id).values())
            if len(estados)>0:
                estado=estados[0]
                datos={'message':"Correcto", 'estado': estado}
            else:
                datos={'message': "estado Venta no encontrado..."}
            return JsonResponse(datos)
        else:
            estados = list(EstadoVenta.objects.values())
            if len(estados)>0:
                datos={'message':"Correcto", 'estados': estados}
            else:
                datos={'message': "estado Venta no encontrados..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        EstadoVenta.objects.create(
            estado=jd['estado']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)
    

    def put(self, request, id):
        jd=json.loads(request.body)
        EstadoV=list(EstadoV.objects.filter(idEstadoVenta=id).values())
        if len(EstadoV)>0:
            EstadoV=EstadoV.objects.get(idEstadoVenta=id)
            EstadoV.estado=jd['estado']
            EstadoV.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Estado no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        EstadoV = list(EstadoVenta.objects.filter(idEstadoVenta=id).values())
        if len(EstadoV)>0:
            EstadoV.objects.filter(idEstadoVenta=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Estado no encontrado..."}
        return JsonResponse(datos)

##GuiaDespacho##
class GuiadespachoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            guia=list(guia.objects.filter(idGuiaDespacho=id).values())
            if len(guia)>0:
                guia=guia[0]
                datos={'message':"Correcto", 'guia': guia}
            else:
                datos={'message': "guia no encontrada... "}
            return JsonResponse(datos)
        else:
            guia = list(guia.objects.values())
            if len(guia)>0:
                datos={'message':"Correcto", 'guia': guia}
            else:
                datos={'message': "guia no encontradas..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        GuiadespachoView.objects.create(
            idGuiaDespacho=jd['idGuiaDespacho']
            ), 
        datos={'message':"Correcto"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        bodegas=list(Bodega.objects.filter(idBodega=id).values())
        if len(bodegas)>0:
            bodega=Bodega.objects.get(idBodega=id)
            bodega.direccionbodega_id=jd['direccionbodega_id']
            bodega.save()
            datos = {'message': "correcto"}
        else: 
            datos={'message': "Bodega no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        bodegas = list(Bodega.objects.filter(idBodega=id).values())
        if len(bodegas)>0:
            Bodega.objects.filter(idBodega=id).delete()
            datos = {'message': "Correcto"}

        else:
            datos={'message': "Bodega no encontrada..."}
        return JsonResponse(datos)
