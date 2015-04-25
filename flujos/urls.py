
from django.conf.urls import patterns, url
from flujos import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='lista_flujo'),
    url(r'^crear/', login_required(views.CreateFlujos.as_view()), name='crear_flujo'), #new line
    url(r'^borrar/(?P<pk>\d+)$', login_required(views.DeleteFlujos.as_view()), name='borrar_flujo'),
    url(r'^modificar/(?P<pk>\d+)$', login_required(views.UpdateFlujos.as_view()), name='modificar_flujo'),
    url(r'^buscar/$', views.search, name='buscar_flujo'),
)