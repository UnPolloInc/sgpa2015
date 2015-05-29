__author__ = 'chelox'


from django.conf.urls import patterns, url
from mensajes import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^enviados/(?P<pk>\d+)$', login_required(views.EnviadosView.as_view()), name='lista_enviados'),
    url(r'^recibidos/(?P<pk>\d+)$', login_required(views.RecibidosView.as_view()), name='lista_recibidos'),

    url(r'^crear/(?P<pk>\d+)/(?P<usuario>\d+)$', login_required(views.CreateMensaje.as_view()), name='crear_mensaje'), #new line
    #url(r'^/(?P<pk>\d+)$', login_required(views.DeleteProyecto.as_view()), name='borrar_proyecto'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(views.DeleteMensaje.as_view()), name='eliminar_mensaje'),
    url(r'^buscar/$', views.search, name='buscar_mensaje'),
)
