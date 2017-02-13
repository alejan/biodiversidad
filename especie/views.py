from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from especie.forms import UserForm
from .models import Especie


class IndexView(generic.ListView):
    template_name = "especie/index.html"
    context_object_name = "especies"
    model = Especie


class Detalle(DetailView):
    template_name = "especie/detalle.html"
    context_object_name = "especie"
    model = Especie


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            first_name = cleaned_data.get('first_data')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user_model = User.objects.create_user(username=username, password=password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            user_model.save()

            return HttpResponseRedirect(reverse('especie:index'))
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'especie/registro.html', context)


def index(request):
    return render(request, 'especie.views.index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        especies = Especie.objects
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('../')
            else:
                return render(request, 'especie/login.html', {'error_message': 'Your account has been disabled'})
        else:
            render(request, 'especie/login.html', {'error_message': 'Invalid login'})
    return render(request, 'especie/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'especie/login.html', context)
