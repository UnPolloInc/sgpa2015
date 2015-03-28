__author__ = 'alforro'

from django.conf.urls import patterns, url
from usuarios import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='lista_usuario'),
    url(r'^crear$', views.CreateUser.as_view(), name='crear_usuario'), #new line
)
