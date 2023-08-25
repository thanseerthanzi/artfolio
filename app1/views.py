from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'admin.html')

def user(request):
    return render(request, 'user.html')

def create(request):
    return render(request, 'create.html')

def loginform(request):
    return render(request, 'loginform.html')