from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre+''+ self.apellido

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.descripcion+''+ str(self.precio)

class Envio(models.Model):
    calle = models.CharField(max_length=70)
    altura = models.IntegerField()
    ciudad = models.CharField(max_length=20)

    def __str__(self):
        return self.calle+''+ str(self.altura)
    
    ## comentario tutor: revisar models para hacer con class meta - pendiente