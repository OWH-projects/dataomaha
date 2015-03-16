# dataomaha portal page url structure

from django.conf.urls import * 

urlpatterns = patterns('',
    (r'^twitter/(?P<username>[a-zA-Z0-9_-]+)$', 'dataomaha.views.Bio'),
    (r'^twitter', 'dataomaha.views.Social'),
    (r'^', 'dataomaha.views.Main'), 
)
