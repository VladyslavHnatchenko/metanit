"""hello URL Configuration

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
from django.urls import path, re_path
from django.views.generic import TemplateView
from firstapp import views


urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
]

# urlpatterns = [
#     path('', views.index),
#     path('create/', views.create),
# ]

# urlpatterns = [
#     path('', views.index),
#     path('about/', TemplateView.as_view(template_name="about.html")),
#     path('contact/', TemplateView.as_view(template_name="contact.html")),
# ]

# urlpatterns = [
#     path('', views.index),
#     path('about/', views.about),
#     path('contact/', views.contact),
#     path('detail/', views.details),
# ]

# urlpatterns = [
#     path('products/<int:productid>/', views.products),
#     path('users/', views.users),
#     re_path(r'^about', views.about),
#     re_path(r'^contact', views.contact),
#     path('', views.index),
# ]

# urlpatterns = [
#     path('products/', views.products),
#     path('products/<int:productid>/', views.products),
#     path('users/', views.users),
#     path('users/<int:id>/<str:name>/', views.users),
#     path('products/<int:productid>/', views.products),
#     path('users/<int:id>/<name>/', views.users),
#     re_path(r'products/$', views.products),
#     re_path(r'^products/(?P<productid>\d+)/', views.products),
#     re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
#     path('', views.index),
#     re_path(r'^about', views.about),
#     re_path(r'^contact', views.contact),
# ]

# urlpatterns = [
#     path('', views.index),
#     path('about', views.about),
#     path('contact', views.contact),
#     path('admin/', admin.site.urls),
# ]
