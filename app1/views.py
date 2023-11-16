from django.shortcuts import render ,redirect
from app1.models import accounts, artist_tbl
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

 
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
    p = accounts()
    p.userid = request.POST.get('userid')
    p.save()
    return render(request, 'artist_profile.html')

def createartist1(request):
    p = artist_tbl()
    p1 = User()
    p3=accounts()
    
    p.fname = request.POST.get('fname')
    p.lname = request.POST.get('lname')
    p.dob = request.POST.get('dob')
    p.gender = request.POST.get('gender')
    p.state = request.POST.get('state')
    p.district = request.POST.get('district')
    p.phone = request.POST.get('phone')
    p.uname = request.POST.get('uname')
    p.email = request.POST.get('email')
    image = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    file_url = fs.url(filename)
    p.photo = file_url

    p1.username =  request.POST.get('uname')
    p1.first_name = request.POST.get('fname')
    p1.last_name = request.POST.get('lname')
    p1.email = request.POST.get('email')
    password = request.POST.get('pass')
    p1.set_password(password)

    p3.userid=request.POST.get('uname')
    p3.status="artist" #"guest" in guest form
    p1.save()
    p.save()
    p3.save()
    return render(request, 'login_artist.html')

def createguest2(request):
   
    p1 = User()
    p3=accounts()
    
    p3.userid=request.POST.get('uname')
    p3.status="guest"

    p1.username = request.POST.get('uname')
   
    p1.set_password(p1.username)
    p3.save()
    p1.save()
    return render(request, "guest_login.html")
def login1(request):
    username=request.POST.get('uname')
    password=request.POST.get('pass')
    user=authenticate(username=username,password=password)
    request.session['username']=username
    if user is not None and user.is_superuser==1:
        return redirect('/adminHome/')
    elif user is not None and user.is_superuser==0:
        u1=accounts.objects.get(userid=user)
        if u1.status=="guest":
          return redirect('/guestHome/')  
        elif u1.status=="artist":
            return redirect('/artistHome/')
        else:
            pass
    else:
        return HttpResponse("Inavalid user !! 404") 
def adminHome(request):
    return render(request, "admin.html")
def guestHome(request):
    return render(request, "guestHome.html")
def artistHome(request):
    return render(request, "artistHome.html")

def addart(request):
    return render(request, "addart.html")