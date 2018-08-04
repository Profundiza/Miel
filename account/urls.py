from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = "account"

urlpatterns = [
    url(r'^$', views.account, name='account'),
    # TODO change url syntax to ?failed
    url(r'^login//?(?P<failed>[-\w\d]+)/?$', views.login_display, name='login_fail'),
    url(r'^login/$', views.login_display, name='login'),
    url(r'^login_submit/$', views.login_submit, name='login_submit'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.my_logout, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
