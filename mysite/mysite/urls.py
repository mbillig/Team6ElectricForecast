"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^$', views.login_user),
    url(r'^login/', views.login_user),
    url(r'^Dashboard', views.HomeView),
    url(r'^Home/', views.HomeView),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/*', views.login_user),
    url(r'^OpArea/', views.OpAreaView, name='opArea'),
    url(r'^OpAreaDetail/(?P<op_area_name>.*)/$', views.opArea, name='op_area_detail'),
    url(r'^data/(?P<op_area_name>.*)/$', views.dataView),
    url('^register/', views.register_user),
    url('^register_success/(?P<data_folder>.*)/$', views.register_success),
]
