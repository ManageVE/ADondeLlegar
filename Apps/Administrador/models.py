from django.db import models

# Create your models here.

estrella = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

class Estados(models.Model):
    Nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.Nombre

class Municipios(models.Model):
    Nombre = models.CharField(max_length=250)
    Estado = models.ForeignKey("Estados")

    def __str__(self):
        return self.Nombre

class Tipo_Tienda(models.Model):
    Nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.Nombre

class Etiquetas(models.Model):
    Nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.Nombre

class Redes_Sociales(models.Model):
    Facebook = models.CharField(max_length=250)
    Twitter = models.CharField(max_length=250)
    Instagram = models.CharField(max_length=250)

    def __str__(self):
        return self.__class__

class Horarios(models.Model):
    Dia = models.CharField(max_length=250)
    Hora_Inicial = models.TimeField()
    Hora_Final =models.TimeField()

    def __str__(self):
        return self.Dia

class Tiendas(models.Model):
    Nombre = models.CharField(max_length=250)
    Logo = models.FilePathField()
    Lema = models.CharField(max_length=250)
    Descripcion = models.CharField(max_length=250)
    Direccion = models.CharField(max_length=250)
    Latitud =models.CharField(max_length=250)
    Longitud = models.CharField(max_length=250)
    Telefono =models.CharField(max_length=250)
    Cotizacion =models.BooleanField(default=False)
    Cotizacion_Dato = models.CharField(max_length=250, blank=True)
    Precio_Mayoreo = models.BooleanField(default=False)
    Etiqueta = models.ManyToManyField("Etiquetas")
    Tipo = models.ForeignKey("Tipo_Tienda")
    Redes_Sociales = models.ForeignKey("Redes_Sociales")
    Horario = models.ManyToManyField("Horarios")

    def __str__(self):
        return self.Nombre

class Promociones(models.Model):
    Descripcion_Corta = models.CharField(max_length=50)
    Descripcion =models.CharField(max_length=250)
    Fecha_Publicacion = models.DateField
    Fecha_Final = models.DateField
    Imagen = models.ForeignKey("Imagenes")
    Tienda = models.ForeignKey("Tiendas")

    def __str__(self):
        return self.Descripcion_Corta

class Imagenes(models.Model):
    Imagen = models.FileField()
    Tienda = models.ForeignKey("Tiendas")

    def __str__(self):
        return self.Tienda


class Comentarios(models.Model):
    Usuario = models.CharField(max_length=250)
    Estrellas = models.IntegerField("estrella")
    Comentario = models.CharField(max_length=500)
    Tienda = models.ForeignKey("Tiendas")

    def __str__(self):
        return self.Usuario


class Productos(models.Model):
    Nombre = models.CharField(max_length=250)
    Precio = models.CharField(max_length=250)
    Tienda = models.ForeignKey("Tiendas")

    def __str__(self):
        return self.Nombre

class Personas(models.Model):
    Nombre = models.CharField(max_length=250)
    A_Paterno = models.CharField(max_length=250)
    A_Materno = models.CharField(max_length=250)
    Foto = models.FilePathField(max_length=250)
    Giro = models.CharField(max_length=250)
    Correo_Electronico = models.EmailField()
    Telefono = models.CharField(max_length=250)
    Tienda = models.ForeignKey("Tiendas")

    def __str__(self):
        return self.Nombre
