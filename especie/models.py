from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.forms import ModelForm


class Categoria(models.Model):
    def __unicode__(self):
        return 'Categoria: ' + self.nombre

    nombre = models.CharField(max_length=50)


class Especie(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre_gen = models.CharField(max_length=50)
    nombre_cien = models.CharField(max_length=50)
    taxonomia = models.CharField(max_length=50)
    descripcion = models.TextField
    foto = models.ImageField(upload_to='avatar', null=True)


class Comentario(models.Model):
    especie = models.ForeignKey(Especie)
    correo = models.CharField(max_length=50)