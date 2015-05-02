
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
)
