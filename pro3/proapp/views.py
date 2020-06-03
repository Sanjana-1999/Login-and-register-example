from django.shortcuts import render
from proapp.forms import profileInfo,UserInfo
# Create your views here.
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))




def index(request):
    return render(request,"proapp/index.html")

def reg(request):
    registered=False


    if(request.method=="POST"):
           user_form=UserInfo(data=request.POST)
           profile_form=profileInfo(data=request.POST)

           if(user_form.is_valid() and profile_form.is_valid()):
               user=user_form.save()
               user.set_password(user.password)
               user.save()

               profile=profile_form.save(commit=False)
               profile.user = user
               if 'profile_pic' in request.FILES:
                   profile.profile_pic = request.FILES['profile_pic']
               profile.save()
               registered=True

           else:
               print(user_form.errors,profile_form.errors)
    else:
        user_form=UserInfo()
        profile_form=profileInfo()
    return render(request,"proapp/register.html",{"user_form":user_form,"profile_form":profile_form,"registered":registered})



def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")

        else:
            return HttpResponse("invalid")
    else:
        return render(request,"proapp/login.html")
