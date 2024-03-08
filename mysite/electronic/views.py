from django.shortcuts import render,redirect,get_object_or_404
from electronic.models import Item,Category,CartItem,Checkout
from users.models import User
from electronic.forms import ItemForm, CheckoutForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator

# Create your views here.
# ---------------------------- Catergory view ---------------------------------------------
def view_category(request, cat_id):
    if request.user.is_superuser:
        itemlist = Item.objects.filter(
            item_category = cat_id
        )

        # #for pagination
        # paginator = Paginator(itemlist, 4)
        # page = request.GET.get('page')
        # itemlist = paginator.get_page(page)
        # totalpage = itemlist.paginator.num_pages

    elif request.user.is_authenticated and request.user.profile.user_type == 'com_owner':
        itemlist = Item.objects.filter(
            item_category = cat_id,
            company_owner = request.user.id
        )

        # #for pagination
        # paginator = Paginator(itemlist, 4)
        # page = request.GET.get('page')
        # itemlist = paginator.get_page(page)
        # totalpage = itemlist.paginator.num_pages

    elif request.user.is_authenticated and request.user.profile.user_type == 'customer':
        itemlist = Item.objects.filter(
            item_category = cat_id
        )

        # #for pagination
        # paginator = Paginator(itemlist, 4)
        # page = request.GET.get('page')
        # itemlist = paginator.get_page(page)
        # totalpage = itemlist.paginator.num_pages
    
    else:
        itemlist = Item.objects.filter(
            item_category = cat_id
        )

        # #for pagination
        # paginator = Paginator(itemlist, 4)
        # page = request.GET.get('page')
        # itemlist = paginator.get_page(page)
        # totalpage = itemlist.paginator.num_pages

    context = {
        'itemlist':itemlist,
        # 'totalpage':totalpage,
        # 'totalpagelist':[n+1 for n in range (totalpage)]
    }
    return render(request, 'products/products.html', context)


# ---------------------------- home page ---------------------------------------------
def index(request):
    itemlist = Item.objects.all()
    productlist = Item.objects.filter(features_prod = True)
    context = {
        'itemlist':itemlist,
        'productlist':productlist
    }
    return render(request, 'products/index.html', context)

# ---------------------------- products page ---------------------------------------------
def products(request):
    if request.user.is_superuser:
        itemlist = Item.objects.all()

        #for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name)

        #for pagination
        # paginator = Paginator(itemlist, 3)
        # page = request.GET.get('page')
        # itemlist = paginator.get_page(page)
        # totalpage = itemlist.paginator.num_pages
 
    elif request.user.is_authenticated and request.user.profile.user_type == 'com_owner':
        itemlist = Item.objects.filter(company_owner = request.user.id)

        #for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name,company_owner = request.user.id)

        # #for pagination
        # paginator = Paginator(itemlist, 4)
        # page = request.GET.get('page')
        # itemlist = paginator.get_page(page)
        # totalpage = itemlist.paginator.num_pages

    elif request.user.is_authenticated and request.user.profile.user_type == 'customer':
        itemlist = Item.objects.all()

        #for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name)

        # #for pagination
        # paginator = Paginator(itemlist, 4)
        # page = request.GET.get('page')
        # itemlist = paginator.get_page(page)
        # totalpage = itemlist.paginator.num_pages

    else:
        itemlist = Item.objects.all()

        #for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name).order_by('item_price')

        # #for pagination
        # paginator = Paginator(itemlist, 4)
        # page = request.GET.get('page')
        # itemlist = paginator.get_page(page)
        # totalpage = itemlist.paginator.num_pages

    context = {
        'itemlist':itemlist,
        # 'totalpage':totalpage,
        # 'totalpagelist':[n+1 for n in range (totalpage)]
    }
    return render(request, 'products/products.html', context)


# ---------------------------- detail page ---------------------------------------------
def detail(request, item_id):

    item = Item.objects.get(id = item_id)

    context = {
        'item':item
    }

    return render(request, 'products/details.html', context)


# ---------------------------- add item page ---------------------------------------------
def create_item(request):

    form = ItemForm(request.POST or None , request.FILES or None)
    # if request.method == 'POST':
    form.instance.added_by = request.user.username
    if form.is_valid():
        form.save()
        return redirect('products:products')
    
    context = {
        'form':form
    }

    return render(request, 'products/add_item.html', context)


# ---------------------------- delete item page ---------------------------------------------
def delete_item(request, id):

    item = Item.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('products:index')

    context = {
        'item':item
    }

    return render(request,'products/del_item.html',context)


# ---------------------------- update item page ---------------------------------------------
def update_item(request,id):

    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None,request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('products:products')
    
    context ={
        'form': form
    }

    return render(request,'products/add_item.html', context)

# ---------------------------- CART page ---------------------------------------------



def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.item_price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'products/cart.html', context)

def add_to_cart(request, id):
    product = Item.objects.get(pk=id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('products:view_cart')


def remove_from_cart(request, cart_item_id):
    # Logic to remove an item from the cart
    # Example:
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('products:view_cart')


def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)

    # Handle the form submission
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()

    return redirect('products:view_cart')


def checkout_page(request):
    cart_items = CartItem.objects.filter(user=request.user.id)

    if cart_items.exists():  # Check if cart is not empty
        total_price = sum(item.product.item_price * item.quantity for item in cart_items)
    else:
        total_price = 0
        cart_items = []



    form = CheckoutForm(request.user, request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        # Perform any additional processing or redirection as needed
        return redirect('products:index')  # Replace 'order_success' with your success page name
    
    context = {
        'form':form,
        'cart_items': cart_items,
        'total_price': total_price
    }

    return render(request, 'products/checkout.html', context)


def order_checkout(request,id):
    order = Item.objects.get(pk=id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(product=order, user=request.user)
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('products:checkout')


