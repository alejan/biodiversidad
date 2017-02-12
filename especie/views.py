from django.views import generic
from django.views.generic import DetailView

from .models import Especie


class IndexView(generic.ListView):
    template_name = "especie/index.html"
    context_object_name = "especies"
    model = Especie

class Detalle(DetailView):
    template_name = "especie/detalle.html"
    context_object_name = "especie"
    model = Especie