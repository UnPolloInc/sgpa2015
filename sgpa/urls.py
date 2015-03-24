from django.conf.urls import patterns, include, url
from django.contrib import admin
#from secret import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('autenticacion.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login', ),




)
