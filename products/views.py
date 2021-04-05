from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from .models import *
from seller.models import *
from customer.models import *

def addProduct(request):
    if request.method == "POST":
        productname = request.POST["productname"]
        productprice = request.POST["productprice"]
        sellerid = request.POST["sellerid"]
        productdetails = request.POST["productdetails"]

        if Seller.objects.filter(id=sellerid).exists():

            seller = Seller.objects.get(id=sellerid)
            x = TemporaryS.objects.get(id=1)

            if seller.sellerName == x.sellerName and seller.sellerPassword == x.sellerPassword:

                add = Products(sellerId=sellerid,productName=productname,
                               productPrice=productprice,productDetails=productdetails)

                add.save()
                messages.info(request,"Product Added")
                return redirect("addproduct")
            else:
                messages.info(request, "Invalid Seller Id")

        else:
            messages.info(request,"Invalid Seller Id")

    return render(request,'products/addproduct.html')


def showProduct(request):
    if request.method == "GET":

        products = Products.objects.filter()
        context = {'products': products}

        return render(request,'products/showproductlist.html',context)

    return render(request,'products/showproductlist.html')


def orderProduct(request):
    if request.method == "POST":
        productid = request.POST["productid"]
        customerid = request.POST["customerid"]

        if Products.objects.filter(id=productid).exists():

            customer = Customer.objects.get(id=customerid)
            x = TemporaryC.objects.get(id=1)

            if customer.customerName == x.customerName and customer.customerPassword == x.customerPassword:

                y = Products.objects.get(id=productid)

                order = OrderProducts(productName=y.productName, productPrice=y.productPrice,
                                      sellerId=y.sellerId, customerId=customerid)

                order.save()
                messages.info(request,"Product Ordered")
                return redirect("orderproduct")
            else:
                messages.info(request, "Invalid Customer Id")

        else:
            messages.info(request, "Invalid Product Id")

    return render(request,"products/orderproduct.html")


def showOrder(request):
    if request.method == "GET":
        x = TemporaryS.objects.get(id=1)
        seller = Seller.objects.get(Q(sellerName=x.sellerName) & Q(sellerPassword=x.sellerPassword))

        seller_order = OrderProducts.objects.filter(sellerId=seller.id)

        context = {'seller_order': seller_order,'seller':seller}

        return render(request,'products/showorder.html',context)

    return render(request,"products/showorder.html")