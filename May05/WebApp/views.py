from django.contrib import messages
from django.shortcuts import render, redirect
from May.models import CategoryDB, ContactsDB
from May.models import ProductDB
from WebApp.models import UserDB, CartDB
from May.models import OrderDB
from django.db.models import Sum


# Create your views here.

def homepage(request):
    CData = CategoryDB.objects.all()
    PData=ProductDB.objects.all()

    return render(request,'Home.html',{'cat':CData,'pro':PData})

def about(request):
    CData = CategoryDB.objects.all()
    PData=ProductDB.objects.all()
    return render(request,'About.html',{'cat':CData,'pro':PData})

def contact(request):
    CData = CategoryDB.objects.all()
    PData=ProductDB.objects.all()
    return render(request,'Contact.html',{'cat':CData,'pro':PData})

def savecontact(request):
    if request.method=="POST":
        cn = request.POST.get('cname')
        ce=request.POST.get('cemail')
        cs=request.POST.get('csubject')
        cm=request.POST.get('cmessage')
        obj = ContactsDB(CName=cn,CEmail=ce,CSubject=cs,CMessage=cm)
        obj.save()
        return redirect(contact)

def shopproduct(request):
    CData = CategoryDB.objects.all()
    PData=ProductDB.objects.all()
    return render(request,'ShopProducts.html',{'cat':CData,'pro':PData})

def catpro(request,cat_name):
    CData = CategoryDB.objects.all()
    PData=ProductDB.objects.filter(Category=cat_name)
    return render(request,'CatPro.html',{'cat':CData,'pro':PData})

def singlepro(request, dataid):
    CData = CategoryDB.objects.all()
    PData=ProductDB.objects.all()
    SData = ProductDB.objects.get(id=dataid)
    return render(request,'SingleProduct.html',{'cat':CData,'pro':PData,'spro':SData})

def cart(request):
    CartData=CartDB.objects.filter(Uname=request.session['username'])
    return render(request,'Cart.html',{'data':CartData})

def ureg(request):
    return render(request,'Registration.html')

def saveuser(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        ue=request.POST.get('uemail')
        up=request.POST.get('uphone')
        upw=request.POST.get('upassword')
        ui = request.FILES['uimg']
        obj = UserDB(Uname=un,UEmail=ue,UPhone=up,UPassword=upw,UImage=ui)
        obj.save()
        messages.success(request, "Successfully Registered")
        return redirect(ureg)

def maylogin(request):
    return render(request,'MayLog.html')

def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('upassword')
        if UserDB.objects.filter(Uname=uname,UPassword=pwd).exists():
            request.session['username']=uname
            request.session['password']=pwd
            messages.success(request, "Successfully Logged In")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid Username Or Password")
            return redirect(ureg)
    return redirect(ureg)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(maylogin)

def savecart(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pn=request.POST.get('product')
        pd = request.POST.get('pdesc')
        pq = request.POST.get('qty')
        pr=request.POST.get('tprice')
        # pimg = request.FILES['img']
        obj = CartDB(Uname=un,Product=pn,PDescription=pd,Quantity=pq,Price=pr)
        obj.save()
        messages.success(request, "Added To Cart...!")
    return redirect(cart)

def deleteitem(request,dataid):
    data=CartDB.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Item Removed From Cart...!")
    return redirect(cart)

def checkout(request):
    return render(request,'CheckOut.html')

def orderplace(request):
    if request.method=="POST":
        fn= request.POST.get('fname')
        ln=request.POST.get('lname')
        em=request.POST.get('email')
        phn=request.POST.get('phone')
        ad1=request.POST.get('adl1')
        ad2=request.POST.get('adl2')
        cn=request.POST.get('country')
        cy=request.POST.get('city')
        st=request.POST.get('state')
        pn=request.POST.get('pin')
        obj = OrderDB(FName=fn,LName=ln,Email=em,Phone=phn,AddrsLine1=ad1, AddrsLine2=ad2,Country=cn,City=cy,State=st,PinCode=pn)
        obj.save()
        messages.success(request, "Order Placed Successfully")
        return redirect(homepage)
