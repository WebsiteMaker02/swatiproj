"""swatiproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, re_path,include
from swatiapp.views import index, cause, contact, about, team,blog
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  re_path(r'^index/$', index, name='index'),
                  re_path(r'^cause/$', cause, name='cause'),
                  re_path(r'^contact/$', contact, name='contact'),
                  re_path(r'^about/$', about, name='about'),
                  re_path(r'^team/$', team, name='team'),
                  re_path(r'^blog/$', blog, name='blog'),
                  path('', index, name="index"),
                  # path('restapi', include('swatiapp.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
