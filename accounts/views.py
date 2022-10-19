
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, profiles


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, "your are already loged in")
        return redirect("/")
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            forms = profiles(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "registered successfull continue to login")
                return redirect('../login')
            else:
                messages.success(
                    request, "registered successfull continue to login")

        return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "your are already logged in")
        return redirect("/")
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticated(request, username=name, password=passwd)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in")
                return redirect("/")
            else:
                messages.error(request, "invalid username and password")
                return redirect("/login")
        return render(request, "registration/login.html")


@login_required
def profile(request):
    return render(request, 'profile.html')

def EditProfile(request):
    form = profiles()
    if request.method == "POST":
        image = request.POST.get('image')
        bio = request.POST.get('bio')
        form = profiles(image,bio)
        form.save()
    return render(request, 'profile.html')