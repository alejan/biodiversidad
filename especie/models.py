from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Especie(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre_general = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=100)
    taxonomia = models.CharField(max_length=50)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='especies', null=True)

    def __unicode__(self):
        return self.nombre_general


class Comentario(models.Model):
    especie = models.ForeignKey(Especie)
    comentario = models.TextField()
    correo = models.EmailField()

    def __unicode__(self):
        return self.especie.nombre_general + ' ' + self.correo + ' ' + self.comentario
