from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^nextmatch/$', views.nextmatch, name='nextmatch'),
        url(r'^team/$', views.teaminfo, name='team'),
        url(r'^info/$', views.userinfo, name='userinfo')
        )