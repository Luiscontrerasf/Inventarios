from django.db import models

# Create your models here.

#fs = FileSystemStorage(location='/media/photos')

class producto(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=30) 
    descripcion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="productos", null = True)
    ingreso = models.IntegerField(verbose_name='Cantidad Ingresada')
    ubicacion_actual = models.CharField(verbose_name='Ubicacion Actual',max_length=15, null=True)
        
    def __str__(self):
        return self.name + ' ' + self.descripcion + ' ' + self.ubicacion_actual  




opciones_consultas = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]
class conacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre