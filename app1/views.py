from django.shortcuts import render

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

