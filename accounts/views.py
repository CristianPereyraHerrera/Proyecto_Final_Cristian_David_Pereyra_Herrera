from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def login_account(request):
    if request.method == "POST":
        my_form = AuthenticationForm(request, data=request.POST)
        if my_form.is_valid():
            information = my_form.cleaned_data
            user = authenticate(username=information['username'], password=information['password'])
            if user:
                login(request, user)
                return redirect('AppEdukateIndex')
            else:
                return redirect('AppEdukateContact')
    my_form = AuthenticationForm()
    context = {
        "my_form": my_form
    }
    return render(request, "accounts/login.html", context=context)
