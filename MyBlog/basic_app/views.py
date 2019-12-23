from django.shortcuts import render
from basic_app.forms import UserInfoForm,UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'basic_app/basic_app.html')

def user_registration(request):
    registered=False

    #user_form=UserProfileInfo()
    #profile_form=UserProfileInfoForm()

    if request.method=="POST":
        user_form=UserInfoForm(request.POST)
        profile_form=UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)#**************IMPORANT****************
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic'in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserInfoForm()
        profile_form=UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
                {'user_form':user_form,
                'profile_form':profile_form,
                'registered':registered})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account isn't active")
        else:
            return HttpResponse("Invalid login details!")
    else:
        return render(request,'basic_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
