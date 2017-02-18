from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


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


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
    pais = CountryField()
    ciudad = models.CharField(max_length=100, default='', blank=True)
    foto = models.ImageField(upload_to='perfil', null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()
