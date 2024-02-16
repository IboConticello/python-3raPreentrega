from django.db import models

class ClaseA(models.Model):
    campo_a = models.CharField(max_length=100)

class ClaseB(models.Model):
    campo_b = models.CharField(max_length=100)

class ClaseC(models.Model):
    campo_c = models.CharField(max_length=100)
