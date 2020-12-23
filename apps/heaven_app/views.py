from django.shortcuts import render
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
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)

def details(request):
    return render(request, 'heaven_app/details.html')

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