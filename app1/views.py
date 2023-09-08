from django.shortcuts import render

# Create your views here.
def index(request):
    # return render(request, 'index.html')
    # return render(request, 'admin.html')
    # return render(request, 'user.html')
    # return render(request, 'loginform.html')
    return render(request, 'create.html')


def admin1(request):
    return render(request, 'admin.html')

def user(request):
    return render(request, 'user.html')

def create(request):
    return render(request, 'create.html')

def loginform(request):
    return render(request, 'loginform.html')