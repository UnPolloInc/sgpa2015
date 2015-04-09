__author__ = 'chelox'

from django.conf.urls import patterns, url
from clientes import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='lista_cliente'),
    url(r'^crear$', login_required(views.CreateUser.as_view()), name='crear_cliente'), #new line
    url(r'^borrar/(?P<pk>\d+)$', login_required(views.DeleteUser.as_view()), name='borrar_cliente'),
    url(r'^modificar/(?P<pk>\d+)$', login_required(views.UpdateUser.as_view()), name='modificar_cliente'),
    url(r'^buscar/$', views.search, name='buscar_cliente'),
)
