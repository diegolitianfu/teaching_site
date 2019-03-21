"""mordern_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from download import views as views_download

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.homepage,name='home'),
    url('^/idea/$',views.idea,name='idea'),
    url('^/team/$',views.team,name='team'),
    url('^/content/$',views.content,name='content'),
    url('^/resources/$',views.resources,name='resources'),
    url('^/resources/kejian/$',views.resources_1,name='kejian_info'),
    url('^/resources/anli/$',views.resources_2,name='anli'),
    url('^/resources/qita/$',views.resources_3,name='qita'),
    url('^/activities/$',views.activities,name='activities'),
    url('^/planning/$',views.planning,name='planning'),
    url(r'^/download/kejian/$', views_download.kejian, name='kejian'),
    url(r'^/download/lunwen/$', views_download.lunwen, name='lunwen'),
    url(r'^/download/sheji/$', views_download.sheji, name='sheji'),
    url(r'^/download/qita/$', views_download.download_qita, name='download_qita'),
    url(r'^/download/(?P<filename>.+)$', views_download.download, name='download'),


]
