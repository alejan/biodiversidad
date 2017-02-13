from django.contrib import admin

from .models import Especie, Categoria, Comentario

admin.site.register(Especie)
admin.site.register(Categoria)
admin.site.register(Comentario)
