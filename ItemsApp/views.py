from django.shortcuts import render,redirect
from .models import Items,Cart
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout as logout1
from django.contrib.auth import login as log
from django.contrib import messages
def home(request):
    return render(request,'ItemsApp/home.html',{'new_Arrival':Items.objects.all()})


def items(request,Item_type):
    return render(request,'ItemsApp/items.html',{'Items':Items.objects.filter(Item_type=Item_type),'It':Item_type})


def Each_Item(request,Item_type,Each_Item):
    it = Items.objects.get(Item_Name=Each_Item)
    flag = False
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.POST.get("Add"):
                try:
                    cart_item = Cart(Customer=request.user,Item_Id=it)
                    cart_item.save()
                except:
                    return redirect('cart')
                
            elif request.POST.get("Del"):
                try:
                    cart_item = Cart.objects.get(Customer=request.user.id,Item_Id=it)
                    cart_item.delete()
                except:
                    return redirect('home-page')
        Items_in_cart = Cart.objects.filter(Customer=request.user.id)
        
        for i in Items_in_cart:
            if i.Item_Id.Item_Name==str(it):
                flag = True
                break
        else:
            flag = False
    return render(request ,'ItemsApp/each_item.html',{'Each_Item':it,'flag':flag})


def Ascending_Order(request,Item_types):
    return render(request,'ItemsApp/items.html',{'Items':Items.objects.filter(Item_type=Item_types).order_by(F('Retail_Price').asc()),'It':Item_types})


def Descending_Order(request,Item_types):
    return render(request,'ItemsApp/items.html',{'Items':Items.objects.filter(Item_type=Item_types).order_by(F('Retail_Price').desc()),'It':Item_types})

@login_required
def view_cart(request):
    Cart_Items = Cart.objects.filter(Customer=request.user)
    return render(request,'ItemsApp/cart.html',{"Cart_Items":Cart_Items})

def delete(request,Each_item):
    it = Items.objects.get(Item_Name=Each_item)
    cart_item = Cart.objects.get(Customer=request.user.id,Item_Id=it.id)
    cart_item.delete()
    return redirect("cart")

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            log(request,user)
            return redirect('home-page')
        else:
            messages.error(request,"*UserName or Password is Incorrect")
    return render(request,'ItemsApp/login.html')

def logout(request):
    logout1(request)
    return redirect('login')
