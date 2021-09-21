"""Chandana_Silks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path,include
from ItemsApp import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('CSadminpage/', admin.site.urls),
    path('home/',views.home,name = 'home-page'),
    path('products/<str:Item_type>/',views.items,name = 'items-page'),
    path('products/<str:Item_type>/<str:Each_Item>/',views.Each_Item,name = 'each-item'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<str:Item_types>/lowtohigh',views.Ascending_Order,name = 'ascending-item'),
    path('<str:Item_types>/hightolow',views.Descending_Order,name = 'descending-item'),
    path('',RedirectView.as_view(url = 'home')),
    path('cart/',views.view_cart,name="cart"),
    path("delete/<str:Each_item>",views.delete,name="Delete"),
    re_path('djga/', include('google_analytics.urls')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
