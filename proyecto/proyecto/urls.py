from django.conf.urls import patterns, include, url
from app.views import ProyectoListView, ProyectoDetailView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'app.views.home', name='home'),
    url(r'account', 'app.views.account', name='account'),
    url(r'^proyectos/$', ProyectoListView.as_view(), name='proyectos'),
    url(r'^proyectos/plus/(\d+)$', 'app.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'app.views.minus', name='minus'),
    url(r'^add_project/$', 'app.views.add_project', name='add_project'),
    url(r'^proyectos/(?P<pk>[\d]+)$', ProyectoDetailView.as_view(), name='proyecto'),
    url(r'^comentarios/', include('django.contrib.comments.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
