from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from especie.forms import UserForm, UpdateProfile, PerfilForm, ComentarioForm
from .models import Especie, Comentario, Perfil


class IndexView(generic.ListView):
    template_name = "especie/index.html"
    context_object_name = "especies"
    model = Especie


def detalle_especie(request, id_especie):
    especie = Especie.objects.get(pk=id_especie)
    comentarios = Comentario.objects.filter(especie_id=id_especie)

    context = {
        'especie': especie,
        'comentarios': comentarios,
        'form_comentario': ComentarioForm()
    }

    return render(request, 'especie/detalle.html', context)


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_perfil = PerfilForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user_model = User.objects.create_user(username=username, password=password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            user_model.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserForm()
        form_perfil = PerfilForm()
    context = {
        'form': form,
        'form_perfil': form_perfil
    }
    return render(request, 'especie/registro.html', context)


def perfil(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        form_perfil = PerfilForm(request.POST, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('perfil'))
    else:
        form = UpdateProfile(instance=request.user)
        form_perfil = PerfilForm(instance=request.user.perfil)
    context = {
        'form': form,
        'form_perfil': form_perfil
    }
    return render(request, 'especie/perfil.html', context)


def index(request):
    return render(request, 'especie.views.index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        Perfil.objects.get_or_create(user=user)
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
