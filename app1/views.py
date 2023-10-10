from django.shortcuts import render ,redirect
from app1.models import guest_tbl, artist_tbl
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
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

def addguest(request):
    p = guest_tbl()
    p.userid = request.POST.get('userid')
    p.save()
    return render(request, 'guest_login.html')

def createartist(request):
    p = artist_tbl()
    p1 = User()
    p.uname = request.POST.get('uname')
    p.fname = request.POST.get('fname')
    p.lname = request.POST.get('lname')
    p.gender = request.POST.get('gender')
    p.email = request.POST.get('email')
    p.phone = request.POST.get('phone')
    p.district = request.POST.get('district')
    p.ads = request.POST.get('ads')
    p.save()
    p1.username = request.POST.get('uname')
    p1.first_name = request.POST.get('fname')
    p1.last_name = request.POST.get('lname')
    p1.email = request.POST.get('email')
    password = request.POST.get('password')
    p1.set_password(password)
    p1.save()
    return render(request, 'login_artist.html')