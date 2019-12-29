from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

def welcome(request):
    if request.user.is_authenticated:
        return mainPage(request)
    else:
        return render(request, 'welcome.html')

@login_required
def mainPage(request):
    return render(request, 'mainPage.html')

# not working def as it is stopped from urls.py
def login(request):
    if request.method == 'POST':
        # Sign in button is pushed
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        user = authenticate(username=request.POST.get('username', None), password=request.POST.get('password', None))
        if user is None:
            # Wrong credentials
            context = {'error': 'Wrong credentials!'}
        else:
            # Correct credentials
            context = None
        return auth_views.LoginView.as_view(template_name='login.html', extra_context = context)(request)
    else:
        # Get request -> load the page
        return render(request, 'login.html')
