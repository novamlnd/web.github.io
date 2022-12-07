"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from faperta.views import prodi
from feb.views import prodi
from fh.views import prodi
from fisip.views import prodi
from fk.views import prodi
from fkip.views import prodi
from ft.views import prodi
from pascasarjana.views import prodi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', prodi),
    path('feb/', prodi),
    path('fh/', prodi),
    path('fisip/', prodi),
    path('fk/', prodi),
    path('fkip/', prodi),
    path('ft/', prodi),
    path('pascasarjana/', prodi),
]
