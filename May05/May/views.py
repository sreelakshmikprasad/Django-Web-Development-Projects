from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

from May.models import CategoryDB, ProductDB , ContactsDB



# Create your views here.

def indexpage(request):
    return render(request,'indexp.html')

def addcategory(request):
    return render(request,'AddCategory.html')

def savecat(request):
    if request.method=="POST":
        cn = request.POST.get('category')
        des = request.POST.get('description')
        pic = request.FILES['catimage']
        obj = CategoryDB(Category=cn,Description=des,Category_Image=pic)
        obj.save()
        messages.success(request,"Category Saved...!")
        return redirect(addcategory)

def displaycategory(request):
    CData = CategoryDB.objects.all()
    return render(request, 'DisplayCategory.html', {'data': CData})

def editcategory(request,dataid):
    CatData=CategoryDB.objects.get(id=dataid)
    return render(request,'EditCategory.html',{'data':CatData})

def updatecat(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('category')
        des = request.POST.get('description')
    try:
        pic=request.FILES['catimage']
        fs = FileSystemStorage()
        file = fs.save(pic.name,pic)
    except MultiValueDictKeyError:
        file=CategoryDB.objects.get(id=dataid).Category_Image
    CategoryDB.objects.filter(id=dataid).update(Category=cn,Description=des,Category_Image=file)
    messages.success(request, "Updated Category Details...!")
    return redirect(displaycategory)

def deletecategory(request,dataid):
    data=CategoryDB.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Category Deleted...!")
    return redirect(displaycategory)

def addproduct(request):
    data=CategoryDB.objects.all()
    return render(request,'AddProduct.html',{'data':data})

def savepro(request):
    if request.method=="POST":
        pc = request.POST.get('pcategory')
        pn=request.POST.get('product')
        pr=request.POST.get('price')
        pd = request.POST.get('pdescription')
        br=request.POST.get('brand')
        img = request.FILES['proimage']
        obj = ProductDB(Category=pc,Product=pn,Price=pr,PDescription=pd,Brand=br,Product_Image=img)
        obj.save()
        messages.success(request, "Product Saved...!")
        return redirect(addproduct)

def displayproduct(request):
    PData = ProductDB.objects.all()
    return render(request, 'DisplayProduct.html', {'data': PData})

def editpro(request,dataid):
    CatData=CategoryDB.objects.all()
    ProData=ProductDB.objects.get(id=dataid)
    return render(request,'EditProduct.html',{'data':ProData,'cat':CatData})

def updatepro(request,dataid):
    if request.method=="POST":
        pc = request.POST.get('pcategory')
        pn = request.POST.get('product')
        pr = request.POST.get('price')
        pd = request.POST.get('pdescription')
        br = request.POST.get('brand')
    try:
        img = request.FILES['proimage']
        fs = FileSystemStorage()
        file = fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=ProductDB.objects.get(id=dataid).Product_Image
    ProductDB.objects.filter(id=dataid).update(Category=pc,Product=pn,Price=pr,PDescription=pd,Brand=br,Product_Image=file)
    messages.success(request, "Updated Product Details...!")
    return redirect(displayproduct)

def deletepro(request,dataid):
    data=ProductDB.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Product Deleted...!")
    return redirect(displayproduct)

def adminlogin(request):
    return render(request,'AdminLogin.html')

def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pwd=request.POST.get('pass')
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully Logged In")
                request.session['username']=uname
                request.session['password']=pwd
                return redirect(indexpage)
            else:
                messages.error(request,"Invalid Username Or Password")
                return redirect(adminlogin)
        else:
            messages.error(request, "Invalid Username Or Password")
            return redirect(adminlogin)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)

def displaycontact(request):
    CData = ContactsDB.objects.all()
    return render(request, 'DisplayContact.html', {'data': CData})

