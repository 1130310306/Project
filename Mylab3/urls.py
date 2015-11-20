"""Mylab3 URL Configuration

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
from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    url(r'^t/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': 'Mylab3app' }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Mylab3app.views.Home'),
    url(r'^home/$', 'Mylab3app.views.Home'),
    url(r'^book/$', 'Mylab3app.views.Books_show'),
    url(r'^author/$', 'Mylab3app.views.Author_find'),
    url(r'^update/$', 'Mylab3app.views.update'),
    url(r'^delete/$', 'Mylab3app.views.delete'),
    url(r'^details/$', 'Mylab3app.views.details'),
    url(r'^addbook/$', 'Mylab3app.views.addbook'),
    url(r'^addauthor/$', 'Mylab3app.views.addauthor'),

]
urlpatterns += staticfiles_urlpatterns()