
from django.conf.urls import patterns, url
from us import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^configurar/(?P<pk>\d+)$', login_required(views.IndexView.as_view()), name='lista_us'),
    url(r'^crear/(?P<pk>\d+)$', login_required(views.Createus.as_view()), name='crear_us'), #new line
    url(r'^borrar/(?P<pk>\d+)$', login_required(views.Deleteus.as_view()), name='borrar_us'),
    url(r'^modificar/(?P<pk>\d+)$', login_required(views.Updateus.as_view()), name='modificar_us'),
    url(r'^priorizar/(?P<pk>\d+)$', login_required(views.PriorizarUs.as_view()), name='priorizar_us'),
    url(r'^buscar/', views.search, name='buscar_us'),
    url(r'^asignar/(?P<pk>\d+)$', login_required(views.Asignacion.as_view()), name='asignar_us'),
    url(r'^registrar/(?P<proyecto>\d+)/(?P<pk>\d+)$', login_required(views.createRegistro.as_view()), name='crearRegistro'),
    url(r'^listar_registro/(?P<proyecto>\d+)/(?P<us>\d+)$', login_required(views.registroView.as_view()), name='listar_registro'),
    url(r'^estado/(?P<pk>\d+)$', login_required(views.CambiarEstadoUs.as_view()), name='cambiar_estado'),
    url(r'^aprobados/(?P<pk>\d+)$', login_required(views.IndexViewAprobados.as_view()), name='aprobado_us'),
    url(r'^aprobar/(?P<pk>\d+)$', login_required(views.Aprobar.as_view()), name='aprobar_us'),
    url(r'^cancelar/(?P<pk>\d+)$', login_required(views.CancelarUs.as_view()), name='cancelar_us'),
    url(r'^release/(?P<pk>\d+)$', login_required(views.IndexViewRelease.as_view()), name='release_us'),

)


