from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import SignUpForm,ProductForm,CategoryForm
from .models import Product,Category
from datetime import datetime
from django.contrib.auth.models import Group
from django.contrib import messages

# Create your views here.

def Home(request):
    products = Product.objects.all()
    categories = Category.objects.all()



    context = {'products' : products,
               'categories': categories
               }
    return render(request,'home.html',context)


def Sign_in(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Login')
    
    else:
        form = SignUpForm()


    context = {'form':form}
    return render(request,'Forms/signUp-form.html',context)

def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username , password = password)
        if user != None :
            login(request,user)
            return redirect('Home')

    return render(request,'Forms/login-form.html')

def Logout(request):
    logout(request)
    return redirect('Home')

def Add_Category(request):
     
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = CategoryForm()

    context = {'form':form}
    return render(request,'Admin_activity/Add-category.html',context)

def Edit_Category(request,cat_id):
    page = "Edit-Category"
    category = Category.objects.get(id = cat_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = CategoryForm(instance=category)

    context = {'form':form,
               'page' : page,
               'category' : category}
    return render(request,'Admin_activity/Add-category.html',context)

def Delete_Category(request,cat_id):
    category = Category.objects.get(id = cat_id)
    if request.method == 'POST':
        category.delete()
        return redirect('Home')
    return render(request,'Forms/delete-form.html',{'category':category})

def Add_Products(request):
    page = "Add-Product"
    user = request.user
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product_form = form.save(commit=False)
            product_form.host = user
            product_form.published = datetime.now()
            product_form.save()
            return redirect('Home')
    else:
        form = ProductForm()
    
    
    context = {'form':form,
               'page':page
               }
    return render(request,'Admin_activity/Add-product.html',context)

def Edit_Product(request,product_id):
    page = "Edit-Product"
    product = Product.objects.get(id = product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
          form.save()
          return redirect('Home')
    else: 
        form = ProductForm(instance=product)
        
    context = {'form':form,
                'page':page} 
    return render(request,'Admin_activity/Add-product.html',context)


def Delete_Product(request,product_id):
    page = "Delete-Product"
    product = Product.objects.get(id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('Home')
    return render(request,'Forms/delete-form.html',{'product':product,'page':page})
        


def Products(request,product_id):
    product = Product.objects.get(id = product_id)

    context = {'product' : product
               }
    return render(request,'Product.html',context)  


def Products_by_categories(request,cat_id):
    category = Category.objects.get(id = cat_id)
    products = Product.objects.filter(category = category)

    context = {'products' : products,'category' : category}
    return render(request,'User_activity/Products_page.html',context)