from django import forms
from django.contrib.auth.models import User

from especie.models import Perfil, Comentario


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('foto', 'pais', 'ciudad', 'bio')


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('correo', 'comentario')
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }
