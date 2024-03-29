from django.shortcuts import render,redirect
from .models import Customer,TemporaryC
from django.contrib import messages
from django.db.models import Q

def homePage(request):
    return render(request,"home/home.html")

def register(request):
    return render(request,'home/customerregistration.html')


def signUp(request):

    if request.method == 'GET':
        return render(request, "customer/customersignup.html")

    else:
        username = request.POST["username"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]
        image = request.FILES.get("customer_img")


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
                                                customerContact=contact,customerPassword=password,customerImage=image)#customer img

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

                temporary_info = TemporaryC(id=1,customerName=username, customerPassword=password)
                temporary_info.save()

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


def customerprofile(request):

    x = TemporaryC.objects.get(id=1)
    customer = Customer.objects.get(Q(customerName=x.customerName) & Q(customerPassword=x.customerPassword))
    context = {"customer": customer}

    return render(request,"customer/profile.html",context)

def profile_update(request):
    if request.method == 'GET':
        return render(request,"customer/profile_update.html")

    elif request.method == 'POST':

        name = request.POST['Cusername']
        Email = request.POST['Cemail']
        Number = request.POST['Cnumber']
        password = request.POST['Mpassword']
        REpassword = request.POST['Rpassword']

    if password ==REpassword:
        x = TemporaryC.objects.get(id=1)
        customer = Customer.objects.get(Q(customerName=x.customerName) & Q(customerPassword=x.customerPassword))
        customer.customerName = name
        customer.customerEmail = Email
        customer.customerContact = Number
        customer.customerPassword = password
        x.customerName = name
        x.customerPassword = password
        customer.save()
        x.save()
        context = {"customer": customer}
        return render(request,"customer/profile.html",context)
    else:
        messages.info(request,"Password Not Same")
        return redirect('profileupdate')


def customerLogout(request):

    x = TemporaryC.objects.get(id=1)
    x.delete()

    return redirect('home')