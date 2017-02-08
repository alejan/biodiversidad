from django.views import generic

from .models import Especie


class IndexView(generic.ListView):
    template_name = "especie/index.html"
    context_object_name = "especies"
    model = Especie

