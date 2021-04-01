"""Agro_Need URL Configuration

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
from django.urls import path
from customer import views as cviews
from seller import views as sviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cviews.homePage,name="home"),

    path('sellerregistration/', sviews.register,name="sellerregistration"),
    path('sellersignup/', sviews.signUp,name="sellersignup"),
    path('sellerlogin/', sviews.login,name="sellerlogin"),
    path('customerlogin/sellerprofile', sviews.sellerprofile,name="sellerprofile"),


    path('customerregistration/', cviews.register,name="customerregistration"),
    path('customersignup/', cviews.signUp,name="customersignup"),
    path('customerlogin/', cviews.login,name="customerlogin"),
    path('customerlogin/customerprofile', cviews.profile,name="customerprofile"),
]
