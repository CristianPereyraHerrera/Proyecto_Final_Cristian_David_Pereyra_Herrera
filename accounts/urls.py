from django.urls import path, include
from accounts.views import login_account
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', login_account, name="loginAccount"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logoutAccount"),
]
