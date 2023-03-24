from django.shortcuts import redirect
from django.urls import reverse


class LoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == reverse('loginAccount') and request.method == 'GET':
            redirect_url = request.GET.get('next')
            if redirect_url:
                request.session['login_redirect_url'] = redirect_url
            else:
                request.session.pop('login_redirect_url', None)

        response = self.get_response(request)

        if request.user.is_authenticated and 'login_redirect_url' in request.session:
            redirect_url = request.session.pop('login_redirect_url')
            return redirect(redirect_url)

        return response
