from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
# Create your views here.
def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('login username & password',username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.WARNING, "Incorrect credentials")
            return redirect('login')

    return render(request,'userauth/login.html')

def user_register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        profile_pic = request.FILES['profile_pic']
        print(fname,lname,email,username,password,profile_pic)
        
        user = User.objects.create_user(username=username, 
                                 email=email, 
                                 first_name=fname, 
                                 last_name=lname, 
                                 password=password)
        user.save()
        profile = Profile.objects.create(user=user,image=profile_pic)
        profile.save()
        return redirect('login')

    return render(request,'userauth/register.html')


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context={'profile':profile}
    return render(request,'userauth/profile.html',context)

def user_logout(request):
    logout(request)
    return redirect('login')

