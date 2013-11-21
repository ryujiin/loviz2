from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loviz2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contab/$', 'contab.views.home',name='resumen'),
    url(r'^contab/materiales/$', 'contab.views.materiales',name='materiales'),
    url(r'^contab/materiales/add/$', 'contab.views.add_material',name='add material'),
    url(r'^contab/compras/$', 'contab.views.compras',name='compras'),
    url(r'^contab/compras/add/$', 'contab.views.add_compras',name='nueva compra'),

    url(r'^admin/', include(admin.site.urls)),
)
