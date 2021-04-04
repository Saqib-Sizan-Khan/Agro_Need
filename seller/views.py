from django.shortcuts import render,redirect
from .models import Seller,TemporaryS
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def register(request):
    return render(request,'home/sellerregistration.html')


def signUp(request):

    if request.method == 'GET':
        return render(request, "seller/sellersignup.html")

    else:
        username = request.POST["username"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]

        if password == password_repeat:
            if Seller.objects.filter(sellerName=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('sellersignup')
            elif Seller.objects.filter(sellerEmail=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('sellersignup')
            elif contact=="":
                messages.info(request, "Empty fields")
                return redirect('sellersignup')
            else:
                seller_info = Seller(sellerName=username, sellerEmail=email,sellerContact=contact,
                                     sellerPassword=password,rating=0)

                seller_info.save()
                return redirect("sellerlogin")

        else:
            messages.info(request, "password not match")
            return redirect('sellersignup')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Seller.objects.filter(sellerName=username).exists():
            if Seller.objects.filter(sellerPassword=password).exists():

                seller = Seller.objects.get(Q(sellerName=username) & Q(sellerPassword=password))

                temporary_info = TemporaryS(id=1,sellerName=username, sellerPassword=password)
                temporary_info.save()

                context = {"seller": seller}
                return render(request,"seller/sellerprofile.html",context)

            else:
                messages.info(request,"Invalid Password")
                return redirect("sellerlogin")
        else:
            messages.info(request, "Invalid Username")
            return redirect("sellerlogin")

    else:
        return render(request, "seller/sellerlogin.html")


def sellerprofile(request):

    x = TemporaryS.objects.get(id=1)
    seller = Seller.objects.get(Q(sellerName=x.sellerName) & Q(sellerPassword=x.sellerPassword))
    context = {"seller": seller}

    return render(request,"seller/sellerprofile.html",context)


def sellerLogout(request):

    x = TemporaryS.objects.get(id=1)
    x.delete()

    return redirect('home')