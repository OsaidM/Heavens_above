from django.shortcuts import render

# Create your views here.
def root(request):
    return render(request, 'heaven_app/index.html')

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