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
    url(r'^ejecutar_sprint/(?P<pk>\d+)$', login_required(views.EjecutarSprint.as_view()), name='ejecutar_sprint'),
    url(r'^finalizar_sprint_list/(?P<pk>\d+)$', login_required(views.IndexViewEnEjecucion.as_view()), name='finalizar_sprint_list'),
    url(r'^finalizado/(?P<pk>\d+)$', login_required(views.IndexViewFinalizado.as_view()), name='sprint_finalizado_list'),
    url(r'^finalizar_confirm/(?P<pk>\d+)$', login_required(views.FinalizarSprint.as_view()), name='finalizar_confirm'),
    url(r'^buscar/(?P<pk>\d+)$', views.search, name='buscar_sprint'),
    url(r'^chart_xtrem/$', views.olaquease, name='xtrem'),
)
