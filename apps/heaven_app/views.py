from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator #import Paginator

# Create your views here.
def root(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'product': page_obj,
    }
    
    return render(request, 'heaven_app/index.html',context)

def search(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    print(query, '/*' *15)
    if query:
        products = products.filter(title__contains = query)
    paginator = Paginator(products, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'product': page_obj,
    }
    
    return render(request, 'heaven_app/search.html',context)


def autocomplete(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(title__istartswith=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.title)
        return JsonResponse(titles, safe=False)

def details(request,p_id):
    this_product = Product.objects.get(id=p_id)
    userslike=this_product.like.all()
    reviews=Review.objects.all()
    request.session['price']= this_product.price
    context= {
        'myproduct': this_product,
        'myreviews': reviews,
        'userslikes': userslike,
    }
    return render(request, 'heaven_app/details.html',context)

def order(request,p_id):
    this_product = Product.objects.get(id=p_id)
    context= {
        'myproduct': this_product,
    }
    return render(request, 'heaven_app/order.html',context)

def post_order(request,p_id):
    this_product = Product.objects.get(id=p_id)
    print(this_product, '/*' *15)
    if request.method == 'POST':
        this_name = request.POST['o_name']
        this_date = request.POST['date_birth']
        this_address = request.POST['address']
        this_phone = request.POST['phone']
        this_price = request.session['price']
        Order.objects.create(name = this_name , date_of_birth =this_date, place_of_birth =this_address, phone = this_phone,total_price = this_price, user_id = User.objects.get(id = 1), product_id = Product.objects.get(id = p_id))
        print(this_price, '/*\/' * 15)
        del request.session['price']
        return redirect('/order/'+format(p_id))
    else:
        return redirect('/')
def signup(request):
    return render(request, 'heaven_app/signup.html')

def admin(request):
    return render(request, 'heaven_app/admin.html')

def account(request):
    return render(request, 'heaven_app/account.html')

def contact(request):
    return render(request, 'heaven_app/contact.html')

def about(request):
    return render(request, 'heaven_app/about.html')
def like(request, p_id):
    this_user = User.objects.get(id=2)
    this_product = Product.objects.get(id=p_id)
    this_user.liked_products.add(this_product)
    return redirect('/details/'+ format(p_id))
def review(request, p_id):
    this_user = User.objects.get(id=2)
    this_product = Product.objects.get(id=p_id)
    content_from_form = request.POST['content']
    Review.objects.create(content=content_from_form,product_id=this_product,user_id=this_user)
    return redirect('/details/'+ format(p_id))