from django.conf.urls import patterns, url

from map import views

urlpatterns = patterns('googlemaps.map.views',
    url(r'^$', views.index, name='index'),
)
