from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^page/(?P<page_title_slug>[\w\-]+)/$', views.page, name='page'),
        
        url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'), # Page for this not done yet.
        
        url(r'^register/$', views.register, name='register'),
        )