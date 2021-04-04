from django.shortcuts import render , redirect , get_object_or_404
from .forms import UserLoginForm , UserRegistrationForm
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from . models import User
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method =="POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , email = cd['email'] , password = cd['password'])
            if user is None:
                messages.error(request , 'Wrong Email or password' , 'danger')
                return redirect('accounts:user_login')
            else:
                login(request , user)
                messages.success(request,'You logged in successfully' , 'success')
                return redirect('products:home')
    else:
        form = UserLoginForm()
        return render(request,'accounts/login.html' , context={'form':form})

def user_registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = User.objects.get(email = cd['email'])
                messages.success(request , 'This Email is already exist')
                return redirect('accounts:user_login')
            except:
                user = User.objects.create_user(full_name=cd['full_name'], email = cd['email'] , password = cd['password'])
                user.save()
                messages.success(request , 'You register successfully' , 'success')
                return redirect('products:home')
    else:
        form = UserRegistrationForm()
        return render(request,'accounts/registration.html' , {'form':form})
    

@login_required
def user_logout(request):
    logout(request)
    messages.success(request , 'You logged out successfully' , 'success')
    return redirect('products:home')


