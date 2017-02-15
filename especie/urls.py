from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detalle/(?P<pk>\d+)/', views.Detalle.as_view(), name='detalle'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]

