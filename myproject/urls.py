"""myproject URL Configuration

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('services',views.services),
    path('save',views.save),
    path('read',views.read),
    path('employees',views.read),
    #path('update',views.update),
    path('delete/<int:id>',views.delete),
    path('insert',views.insert),
    path('edit/<int:id>',views.edit),
    path('edit/update',views.update),
    path('login',views.signin,name='signin'),
    path('loggin',views.loggin),
    path('logout',views.loggout),
    path('form',views.insertform),
]
