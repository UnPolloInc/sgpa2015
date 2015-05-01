__author__ = 'chelox'


from django.conf.urls import patterns, url
from sprint import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^configurar/(?P<pk>\d+)$', login_required(views.IndexView.as_view()), name='lista_sprint'),
    url(r'^crear/(?P<pk>\d+)$', login_required(views.CreateSprint.as_view()), name='crear_sprint'), #new line
    #url(r'^borrar/(?P<pk>\d+)$', login_required(views.DeleteProyecto.as_view()), name='borrar_sprint'),
    url(r'^modificar/(?P<pk>\d+)$', login_required(views.UpdateSprint.as_view()), name='modificar_sprint'),
    url(r'^buscar/$', views.search, name='buscar_sprint'),
)
