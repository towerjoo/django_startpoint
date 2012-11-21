from django.conf.urls import patterns, include, url
from django.conf import settings



urlpatterns = patterns('sample.views',
    url(r'^$', 'index', name="sample-index"),
)

