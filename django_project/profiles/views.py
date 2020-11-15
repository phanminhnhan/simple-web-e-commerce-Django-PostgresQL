from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import TemplateView
from django.http import HttpResponse


def register_views(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("homepage")
    else:
        form = UserRegisterForm()
        return render(request, 'register.html', {'form':form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('homepage')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            username = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, 'successfully')
                return redirect('homepage')
            else:
                messages.error(request, 'invalid username or password')
        else:
            messages.error(request, 'invalid username or password')

    form = AuthenticationForm()
    return render(request,
                  "login.html",
                  {'form': form}
                  )



