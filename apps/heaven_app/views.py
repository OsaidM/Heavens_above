<<<<<<< HEAD
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator #import Paginator

=======
from django.shortcuts import render,redirect
from .models import *
>>>>>>> 9da95145cbb68f69d77786061732ecba446db90e
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
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)

def details(request):
    this_product = Product.objects.get(id=2)
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
def like(request):
    this_user = User.objects.get(id=2)
    this_product = Product.objects.get(id=2)
    this_user.liked_products.add(this_product)
    return redirect('/details')
def review(request):
    this_user = User.objects.get(id=2)
    this_product = Product.objects.get(id=2)
    content_from_form = request.POST['content']
    Review.objects.create(content=content_from_form,product_id=this_product,user_id=this_user)
    return redirect('/details')
    