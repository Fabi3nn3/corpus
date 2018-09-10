from django.conf.urls import url
from . import views

urlpatterns = [
    #default homepage, index for each ind. app
    url(r'^$', views.index, name='index'),
]
