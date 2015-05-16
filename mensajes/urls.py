__author__ = 'chelox'


from django.conf.urls import patterns, url
from mensajes import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^configurar/(?P<pk>\d+)$', login_required(views.IndexView.as_view()), name='lista_mensaje'),
    url(r'^crear/(?P<pk>\d+)/(?P<usuario>\d+)$', login_required(views.CreateMensaje.as_view()), name='crear_mensaje'), #new line
    #url(r'^/(?P<pk>\d+)$', login_required(views.DeleteProyecto.as_view()), name='borrar_proyecto'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(views.DeleteMensaje.as_view()), name='eliminar_mensaje'),
    url(r'^buscar/$', views.search, name='buscar_mensaje'),
)
