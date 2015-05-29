__author__ = 'alforro'

from django.conf.urls import patterns, url
from proyectos import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='lista_proyecto'),
    url(r'^crear$', login_required(views.CreateProyecto.as_view()), name='crear_proyecto'), #new line
    url(r'^configurar/(?P<pk>\d+)$', login_required(views.ConfigurarProyecto.as_view()), name='configurar'),
    url(r'^modificar/(?P<pk>\d+)$', login_required(views.UpdateProyecto.as_view()), name='modificar_proyecto'),
    url(r'^buscar/$', views.search, name='buscar_proyecto'),
)
