from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listado_especies, name='index'),
    url(r'^categoria/(?P<nombre_categoria>\w+)/$', views.listado_especies, name='por_categorias'),
    url(r'^detalle/(?P<id_especie>\d+)/', views.detalle_especie, name='detalle'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]

