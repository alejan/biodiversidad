from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.db import transaction
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from especie.forms import UserForm, UpdateProfile, PerfilForm, ComentarioForm, CategoriaForm
from .models import Especie, Comentario, Perfil, Categoria


def listado_especies(request, nombre_categoria=None):
    categoria = Categoria.objects.filter(nombre=nombre_categoria).first() if nombre_categoria else None

    if categoria:
        especies = Especie.objects.filter(categoria=categoria)
        form = CategoriaForm(initial={'categoria': categoria})
    else:
        especies = Especie.objects.all()
        form = CategoriaForm()

    return render(request, 'especie/index.html', {
        'especies': especies,
        'form': form,
    })


@csrf_exempt
def listado_especies_rest(request, nombre_categoria=None):
    categoria = Categoria.objects.filter(nombre=nombre_categoria).first() if nombre_categoria else None

    if categoria:
        especies = Especie.objects.filter(categoria=categoria)
    else:
        especies = Especie.objects.all()

    return HttpResponse(serializers.serialize("json", especies))


def detalle_especie(request, id_especie):
    especie = Especie.objects.get(pk=id_especie)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            new_comment = Comentario(especie=especie, comentario=clean_data.get('comentario'),
                                     correo=clean_data.get("correo"))
            new_comment.save()
            return redirect('detalle', id_especie=id_especie)
    else:
        form = ComentarioForm()

    context = {
        'especie': especie,
        'comentarios': Comentario.objects.filter(especie_id=id_especie).order_by('-id'),
        'form_comentario': form
    }

    return render(request, 'especie/detalle.html', context)


@transaction.atomic
def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_perfil = PerfilForm(request.POST, request.FILES)
        if form.is_valid() and form_perfil.is_valid():
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

            perfil_model = user_model.perfil
            perfil_model.foto = form_perfil.cleaned_data['foto']
            perfil_model.pais = form_perfil.cleaned_data['pais']
            perfil_model.ciudad = form_perfil.cleaned_data['ciudad']
            perfil_model.bio = form_perfil.cleaned_data['bio']
            perfil_model.save()
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
        if form.is_valid() and form_perfil.is_valid():
            form.save()
            form_perfil.save()
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
