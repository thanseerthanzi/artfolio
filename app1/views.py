from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    # return render(request, 'index.html')
    # return render(request, 'admin.html')
    # return render(request, 'user.html')
    # return render(request, 'loginform.html')
    return render(request, 'index.html')


def admin1(request):
    return render(request, 'admin.html')

def artistprofile(request):
    return render(request, 'artist_profile.html')

def createartist(request):
    return render(request, 'create_artist.html')

def loginartist(request):
    return render(request, 'login_artist.html')

def guestlogin(request):
    return render(request, 'guest_login.html')

def guestlogin(request):
    p = guest_tbl()
    p1 = guest()
