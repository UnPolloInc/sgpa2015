__author__ = 'jorgeflor'


from django.conf.urls import patterns, url
from sprint import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^configurar/(?P<pk>\d+)$', login_required(views.IndexView.as_view()), name='lista_sprint'),
    url(r'^crear/(?P<pk>\d+)$', login_required(views.CreateSprint.as_view()), name='crear_sprint'), #new line
    #url(r'^borrar/(?P<pk>\d+)$', login_required(views.DeleteProyecto.as_view()), name='borrar_sprint'),
    url(r'^modificar/(?P<pk>\d+)$', login_required(views.UpdateSprint.as_view()), name='modificar_sprint'),
    url(r'^listarus/(?P<pk>\d+)/(?P<sprint>\d+)$', login_required(views.IndexViewUs.as_view()), name='us_listar'),
    url(r'^reasignarus/(?P<pk>\d+)$', login_required(views.ReasignarUs.as_view()), name='reasignar_us'),
    url(r'^cambiar_estado/(?P<pk>\d+)/(?P<sprint>\d+)$', login_required(views.CambiarEstado.as_view()), name='cambiar_estado'),
    url(r'^buscar/(?P<pk>\d+)$', views.search, name='buscar_sprint'),
)
