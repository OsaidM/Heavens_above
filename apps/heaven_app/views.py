from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def root(request):
    return render(request, 'heaven_app/index.html')

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
    