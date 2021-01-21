from django.db import models

# Create your models here.

#fs = FileSystemStorage(location='/media/photos')

class producto(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=30) 
    descripcion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="productos", null = True)
        
    def __str__(self):
        return self.name + ' ' + self.descripcion 


class movimiento(models.Model):
    fecha_ingreso = models.DateTimeField()
    ingreso = models.IntegerField(verbose_name='Cantidad Ingresada')
    fecha_egreso = models.DateTimeField(null=True)
    egreso = models.IntegerField(verbose_name='Cantidad Egresada', null=True)
    ubicacion_actual = models.CharField('Ubicacion Actual',max_length=15, null=True)
    ubicacion_anterior = models.CharField('Ubicacion Anterior',max_length=15,null=True)

    def __str__(self):
        return self.ingreso + ' ' + self.egreso + ' ' + self.ubicacion_actual + ' ' + self.ubicacion_anterior

class stock(models.Model): 
    cantidad = models.IntegerField()

    def __str__(self):
        return self.cantidad