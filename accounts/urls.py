from django.contrib import admin
from django.urls import path, include
from accounts.views import login_account, logout

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_account, name="loginAccount"),
    # path('logout/', logout_account, name="logoutAccount"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logoutAccount"),
]
