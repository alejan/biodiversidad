from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Categoria(models.Model):
    def __unicode__(self):
        return self.nombre

    nombre = models.CharField(max_length=50)


class Especie(models.Model):
    def __unicode__(self):
        return self.nombre_gen

    categoria = models.ForeignKey(Categoria)
    nombre_general = models.CharField(max_length=50)
    nombre_cientifico = models.CharField(max_length=50)
    taxonomia = models.CharField(max_length=50)
    descripcion = models.TextField
    foto = models.ImageField(upload_to='avatar', null=True)


class Comentario(models.Model):
    def __unicode__(self):
        return self.especie.nombre_gen + ' ' + self.correo + ' ' + self.comentario

    especie = models.ForeignKey(Especie)
    comentario = models.TextField
    correo = models.EmailField
