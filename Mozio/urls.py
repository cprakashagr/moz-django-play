"""Mozio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

# from django.contrib import admin
from Mozio.views import providers, polygons, userEndPoints

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^hello/$', providers.hello),

    # Mozio Specific URLS
    url(r'^provider/add/$', providers.addProvider),
    url(r'^provider/delete/$', providers.deleteProvider),
    url(r'^provider/update/$', providers.updateProvider),
    url(r'^provider/get/$', providers.getProvider),

    url(r'^poly/add/$', polygons.addPolygons),
    url(r'^poly/delete/$', polygons.deletePolygons),
    url(r'^poly/update/$', polygons.updatePolygons),
    url(r'^poly/get/$', polygons.getPolygons),

    url(r'^user/search/(\d+\.\d)/(\d+\.\d)$', userEndPoints.searchPolygon),

    # url(r'^$', views.hello),
    # url(r'^time/plus/(\d{1,3})/(5)/$', views.hello),
    # url(r'^provider/plus/(\d{1,3})/(5)/$', views.hello),

]
