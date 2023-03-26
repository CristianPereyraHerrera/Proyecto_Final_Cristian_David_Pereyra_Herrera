from django.urls import path
from accounts.views import login_account, register_account
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_account, name="loginAccount"),
    path('register/', register_account, name="registerAccount"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logoutAccount"),
]
