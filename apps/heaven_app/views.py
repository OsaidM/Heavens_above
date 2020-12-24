from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator #import Paginator
import bcrypt

def signup(request):
    return render(request, 'heaven_app/signup.html')

def register(request):
    print('*'*80)
    print("in the register method")
    if request.method =='POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/signup')
        else:
            password=request.POST['password']
            pw_hash=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], address=request.POST['address'], password=pw_hash.decode())
            request.session['user']=request.POST['first_name']
            request.session['user_id']=new_user.id
            return redirect ('/')
    return render(request, 'heaven_app/order.html')

def login(request):
    print('*'*80)
    print("in the login method")
    if request.method =='POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user=User.objects.filter(email=request.POST['login_email'])
            logged_user=user[0]
            request.session['user'] = logged_user.first_name
            request.session['user_id']=logged_user.id
            return redirect ('/')
    else:
        return redirect ('/')


def root(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)
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
    context= {
        'myproduct': this_product,
        'myreviews': reviews,
        'userslikes': userslike,
    }
    return render(request, 'heaven_app/details.html',context)

def order(request):
    return render(request, 'heaven_app/order.html')

def admin(request):
    return render(request, 'heaven_app/admin.html')

def account(request,u_id):
    this_user=User.objects.get(id=u_id)
    context={
        'this_user': this_user
    }
    return render(request, 'heaven_app/account.html',context)

def contact(request):
    return render(request, 'heaven_app/contact.html')

def about(request):
    return render(request, 'heaven_app/about.html')

def logout(request):
    if "user_id" in request.session:
        del request.session["user_id"]
    return redirect('/')
def like(request, p_id):
    this_user = User.objects.get(id=2)
    this_product = Product.objects.get(id=p_id)
    this_user.liked_products.add(this_product)
    return redirect('/details/'+ format(p_id))
def review(request):
    this_user = User.objects.get(id=2)
    this_product = Product.objects.get(id=2)
    content_from_form = request.POST['content']
    Review.objects.create(content=content_from_form,product_id=this_product,user_id=this_user)
    return redirect('/details')

def update(request, u_id):
    print('*'*80)
    print("in the update method")
    if request.method =='POST': 
        updates=User.objects.get(id=u_id)
        updates.first_name=request.POST['first_name']
        updates.last_name=request.POST['last_name']
        updates.email=request.POST['email']
        updates.address=request.POST['address']
        updates.save()
        return redirect (f'/account/{u_id}')
    else:
        return redirect ('/account')