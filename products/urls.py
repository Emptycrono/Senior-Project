from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^products$', views.products),
    url(r'^base$', views.base),
    url(r'^Login$', views.Login)
]