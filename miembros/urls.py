
from django.conf.urls import patterns, url
from miembros import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^configurar/(?P<pk>\d+)$', login_required(views.IndexView.as_view()), name='miembros_listar'),
    url(r'^crear/(?P<pk>\d+)/(?P<usuario>\d+)$', login_required(views.CreateMiembro.as_view()), name='crear_miembro'),
    url(r'^quitar/(?P<pk>\d+)$', login_required(views.DeleteMiembro.as_view()), name='quitar_miembro'),
    url(r'^buscar/(?P<pk>\d+)$', views.search, name='buscar_miembros'),
    url(r'^ver_usuarios/(?P<pk>\d+)$', login_required(views.IndexViewVerUser.as_view(context_object_name='no_miembros')), name='ver_usuarios'),

)