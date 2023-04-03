from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse
from .forms import UserRegisterForm
from .models import Avatar


@login_required()
def edit_user(request):
    user = request.user
    try:
        avatar = Avatar.objects.get(user=user)
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == "POST":
        my_form = UserRegisterForm(request.POST, request.FILES)
        if my_form.is_valid():
            information = my_form.cleaned_data
            if check_password(information["password"], user.password):
                user.username = information["username"]
                user.email = information["email"]
                user.first_name = information["first_name"]
                user.last_name = information["last_name"]
                user.save()

                if avatar is None:
                    avatar = Avatar.objects.create(user=user, image=None, description=None, website=None)

                avatar.image = information['image']
                avatar.description = information['description']
                avatar.website = information['website']
                avatar.save()

                success_message = "Account Edited Successful!"
                messages.success(request, success_message)

                logout(request)

                context = {
                    "title": "Edit Account",
                    "redirect": ('loginAccount')
                }
                return render(request, "accounts/logout.html", context=context)
            else:
                messages.error(request, 'password invalid')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        my_form = UserRegisterForm(initial={
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })

        if avatar is not None:
            my_form.fields['image'].initial = avatar.image
            my_form.fields['description'].initial = avatar.description
            my_form.fields['website'].initial = avatar.website

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
