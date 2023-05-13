from django.db import models

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreComuna = models.CharField(max_length=30, null=False)

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True)
    nombreCalle = models.CharField(max_length=50, null=False)
    numeroCasa = models.IntegerField(null=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True)
    nombreGenero = models.CharField(max_length=50, null=False)

class Consola(models.Model):
    idConsola = models.AutoField(primary_key=True)
    nombreConsola = models.CharField(max_length=50, null=False)

class Producto(models.Model): 
    idProducto = models.AutoField(primary_key=True)
    stock = models.IntegerField(null=False, default=0)
    nombreProducto = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    imagen = models.ImageField(upload_to='')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE) 
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE)
    

class Bodega(models.Model):
    idBodega = models.AutoField(primary_key=True)
    direccionbodega = models.ForeignKey(Direccion, on_delete=models.CASCADE)


class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombreRol = models.CharField(max_length=50, null=False)

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombreEmpleado = models.CharField(max_length=50, null=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombreRegion = models.CharField(max_length=30, null=False)


class Cliente(models.Model): 
    idCliente = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(max_length=100, null=False)
    nombreUsuario = models.CharField(max_length=50, unique=True ,null=False)
    telefono = models.CharField(max_length=12, null=False)
    contraseña = models.CharField(max_length=50, null=False)
    correo = models.CharField(max_length=50, null=False)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    
class MetodoPago(models.Model):
    idMetodoPago = models.AutoField(primary_key=True)
    tipoMetodo = models.CharField(max_length=20, null=False)

class EstadoVenta(models.Model):
    idEstadoVenta = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10, null=False)

class Venta(models.Model): 
    idVenta = models.AutoField(primary_key=True)
    totalPago = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodoPago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    estadoVenta = models.ForeignKey(EstadoVenta, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

class DetalleVenta(models.Model):
    idDetalleVenta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)

class Sucursal(models.Model):
    idSucursal = models.AutoField(primary_key=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

class Pasillo(models.Model):
    idPasillo = models.AutoField(primary_key=True)
    numeroPasillo = models.IntegerField()
    
class Seccion(models.Model):
    idSeccion = models.AutoField(primary_key=True)
    letraSeccion = models.CharField(max_length=1, null=False)
    
class Ubicacion_producto(models.Model):
    idUbicacion = models.AutoField(primary_key=True)
    pasillo = models.ForeignKey(Pasillo, on_delete=models.CASCADE) 
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE) 

class Detalle_bodega(models.Model):
    idDetalleBodega = models.AutoField(primary_key=True)
    bodegaa = models.ForeignKey(Consola, on_delete=models.CASCADE)
    cantidadProd = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    ubicacion_producto = models.ForeignKey(Ubicacion_producto, on_delete=models.CASCADE)
    

class Guia_despacho_detalle(models.Model):
    idGuiaDespacho_detalle = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)

class Guia_despacho(models.Model):
    idGuiaDespacho = models.AutoField(primary_key=True)
    despachador = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fechaEmision = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    guia_despacho = models.ForeignKey(Guia_despacho_detalle, on_delete=models.CASCADE)