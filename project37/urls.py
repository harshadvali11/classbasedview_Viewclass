"""project37 URL Configuration

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('Cbv_string/',Cbv_string.as_view(),name='Cbv_string'),

    path('fbv_page/',fbv_page,name='fbv_page'),
    path('cbv_page/',cbv_page.as_view(),name='cbv_page'),

    path('fbv_form/',fbv_form,name='fbv_form'),
    path('cbv_form/',cbv_form.as_view(),name='cbv_form'),

    path('cbv_template/',cbv_template.as_view(),name='cbv_template'),












]
