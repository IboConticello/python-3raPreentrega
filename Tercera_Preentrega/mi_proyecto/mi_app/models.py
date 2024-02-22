from django.db import models

class ClienteForm(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre+''+ self.apellido

class ProductoForm(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.descripcion+''+ str(self.precio)

class EnvioForm(models.Model):
    calle = models.CharField(max_length=70)
    altura = models.IntegerField()
    ciudad = models.CharField(max_length=20)

    def __str__(self):
        return self.calle+''+ str(self.altura)