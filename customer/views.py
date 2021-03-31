from django.shortcuts import render,redirect
from .models import Customer
from django.contrib import messages
from django.db.models import Q

def homePage(request):
    return render(request,"home/home.html")


def signUp(request):

    if request.method == 'GET':
        return render(request, "customer/customersignup.html")

    else:
        username = request.POST["username"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]

        if password == password_repeat:
            if Customer.objects.filter(customerName=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('customersignup')
            elif Customer.objects.filter(customerEmail=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('customersignup')
            elif contact=="":
                messages.info(request, "Empty fields")
                return redirect('customersignup')
            else:
                customer_info = Customer(customerName=username, customerEmail=email,
                                                customerContact=contact,customerPassword=password)

                customer_info.save()
                return redirect("customerlogin")

        else:
            messages.info(request, "password not match")
            return redirect('customersignup')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Customer.objects.filter(customerName=username).exists():
            if Customer.objects.filter(customerPassword=password).exists():

                customer = Customer.objects.get(Q(customerName=username) & Q(customerPassword=password))

                # temporary_info = TemporarySP(id=1,parentName=username, parentPassword=password)
                # temporary_info.save()

                context = {"customer": customer}
                return render(request,"customer/profile.html",context)

            else:
                messages.info(request,"Invalid Password")
                return redirect("customerlogin")
        else:
            messages.info(request, "Invalid Username")
            return redirect("customerlogin")

    else:
        return render(request, "customer/customerlogin.html")


def profile(request):
    return render(request,"customer/profile.html")