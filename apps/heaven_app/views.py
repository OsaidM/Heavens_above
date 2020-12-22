from django.shortcuts import render

# Create your views here.
def root(request):
    return render(request, 'heaven_app/index.html')
def signup(request):
    return render(request, 'heaven_app/signup.html')

def about(request):
    return render(request, 'heaven_app/about.html')