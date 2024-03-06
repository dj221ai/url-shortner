from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please check.')
            return redirect('account:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!. Please check.')
            return redirect('account:register')
        
        if password1!=password2:
            messages.error(request, "Passwords didn't match. Please check")
            return redirect('account:register')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('account:register')
        

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.first_name=fname
        user.last_name=lname
        # user.username=user.username.lower()
        user.save()
        messages.success(request, 'Hurray!! You Registration is Successful. congrats!!')
        auth_login(request, user)
        return redirect('shortner:index')
    else:
        return render(request, 'account/register.html')



def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('shortner:index')
        else:
            messages.error(request, "Invalid login Credentials!!")
            return redirect('account:signin')
    else:
        return render(request, 'account/login.html')


@login_required
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('shortner:index')
