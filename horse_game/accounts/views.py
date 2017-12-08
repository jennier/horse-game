from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
    
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from horses.models import Horse
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "form.html", {"form":form, "title": title})


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
    
def UserDetail(DetailView):
	model = User
	all_models_dict = {
        "template_name": "user_detail.html",
        "queryset": User,
        "extra_context" : {"horse_list" : Horse.objects.filer(owner=username),
                           "venue_list": Venue.objects.all(),
                           #and so on for all the desired models...
                           }
    }
	