__author__ = 'alforro'

from django.conf.urls import patterns, url
from usuarios import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='lista_usuario'),
    url(r'^crear$', login_required(views.CreateUser.as_view()), name='crear_usuario'), #new line
    url(r'^borrar/(?P<pk>\d+)$', views.DeleteUser.as_view(), name='borrar_usuario'),
    url(r'^modificar/(?P<pk>\d+)$', views.UpdateUser.as_view(), name='modificar_usuario'),
    url(r'^buscar/$', views.search, name='buscar_usuario'),
)
