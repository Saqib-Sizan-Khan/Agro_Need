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
from products import views as pviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cviews.homePage,name="home"),

    #seller url
    path('sellerregistration/', sviews.register,name="sellerregistration"),
    path('sellersignup/', sviews.signUp,name="sellersignup"),
    path('sellerlogin/', sviews.login,name="sellerlogin"),
    path('sellerlogin/sellerprofile', sviews.sellerprofile,name="sellerprofile"),
    path('sellerlogin/logout/',sviews.sellerLogout,name='sellerlogout'),

    #customer url
    path('customerregistration/', cviews.register,name="customerregistration"),
    path('customersignup/', cviews.signUp,name="customersignup"),
    path('customerlogin/', cviews.login,name="customerlogin"),
    path('customerlogin/customerprofile', cviews.customerprofile,name="customerprofile"),
    path('customerlogin/logout/',cviews.customerLogout,name='customerlogout'),

    #product url
    path('sellerlogin/addproduct',pviews.addProduct,name="addproduct"),
    path('customerlogin/showproduct',pviews.showProduct,name="showproduct"),
    path('sellerlogin/showorder',pviews.showOrder,name="showorder"),
    path('customerlogin/buyproduct',pviews.buyProduct,name="buyproduct"),
]
