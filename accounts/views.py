from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse
from accounts.forms import UserRegisterForm
from accounts.models import Avatar


@login_required()
def edit_user(request):
    user = request.user
    if request.method == "POST":
        my_form = UserRegisterForm(request.POST, request.FILES)
        if my_form.is_valid():
            information = my_form.cleaned_data
            if check_password(information["password"], user.password):
                user.username = information["username"]
                user.email = information["email"]

                try:
                    user.avatar.image = information["image"]
                except:
                    avatar = Avatar(user=user, image=information["image"])
                    avatar.save()

                success_message = "Account Edited Successful!"
                messages.success(request, success_message)
                user.save()
                logout(request)
                if messages.success:
                    context = {
                        "title": "Edit Account",
                        "redirect": ('loginAccount')
                    }
                    return render(request, "accounts/logout.html", context=context)
            else:
                messages.error(request, 'password invalid')
        else:
            messages.error(request, 'Please correct the errors below.')
    my_form = UserRegisterForm(initial={
        "username": user.username,
        "email": user.email
    })
    context = {
        "my_form": my_form
    }
    return render(request, "accounts/edit_user.html", context=context)


def register_account(request):
    if request.method == "POST":
        my_form = UserCreationForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect("loginAccount")
    my_form = UserCreationForm()
    context = {
        "my_form": my_form
    }
    return render(request, "AppEdukate/form_students.html", context=context)


# Create your views here.


@user_passes_test(lambda u: not u.is_authenticated, login_url='AppEdukateIndex', redirect_field_name=None)
def login_account(request):
    if request.method == "POST":
        my_form = AuthenticationForm(request, data=request.POST)
        if my_form.is_valid():
            information = my_form.cleaned_data
            user = authenticate(username=information['username'], password=information['password'])
            if user:
                login(request, user)
                success_message = "Login successful!"
                messages.success(request, success_message)
                next_url = request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                elif messages.success:
                    context = {
                        "title": "Login",
                        "redirect": reverse('AppEdukateIndex')
                    }
                    return render(request, "accounts/logout.html", context=context)
                else:
                    return redirect('loginAccount')
            else:
                return redirect('AppEdukateIndex')
    my_form = AuthenticationForm()
    next_url = request.GET.get('next', '/')
    context = {
        "my_form": my_form,
        "next": next_url
    }
    return render(request, "accounts/login.html", context=context)
