from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.noid, name='noid'),
    url(r'^events-with-subscriptions/$', views.noid, name='noid2'),
    url(r'^events-with-subscriptions/(?P<eventid>.+)/$', views.basic, name='basic'),
]