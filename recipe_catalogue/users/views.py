from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Your username or password is incorrect. Please try again."))
            return redirect('login_user')

    else:
        return render(request, 'authenticate/login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout successful"))
    return redirect('home')
   



