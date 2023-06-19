from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
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


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (f"Registration successful - welcome {username}!"))
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {'form':form})

class RegisterUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login_user')
    template_name = 'authenticate/register_user.html'



   



