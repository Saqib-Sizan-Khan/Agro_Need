from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from .models import Products,BuyProducts
from seller.models import Seller,TemporaryS

# Create your views here.

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
