__author__ = 'alforro'


from django.conf.urls import patterns, url
from roles import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', login_required(views.IndexView.as_view()), name='lista_rol'),
    url(r'^crear/(?P<pk>\d+)$', login_required(views.CrearRol.as_view()), name='crear_rol'), #new line
    #url(r'^configurar/(?P<pk>\d+)$', login_required(views.DeleteProyecto.as_view()), name='borrar_proyecto'),
    url(r'^modificar/(?P<pk>\d+)$', login_required(views.UpdateRol.as_view()), name='modificar_rol'),
    url(r'^buscar/(?P<pk>\d+)$', views.search, name='buscar_rol'),
)
