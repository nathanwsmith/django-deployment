from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def welcome(request):
    if request.user.is_authenticated: #loged in user
        return mainPage(request)
    else: # not logged in user
        if request.method == 'POST': #a attempt for sign-up
            email = request.POST.get('email', None)
            return signup(request, email)
        else: # GET request
            if request.GET.get('email') is not None:
                return signup(request, email=request.GET.get('email', None))
            else:
                return render(request, 'welcome.html')

@login_required
def mainPage(request):
    return render(request, 'mainPage.html')

def login(request):
    if request.method == 'POST': # Sign in button is pushed
        if not request.POST.get('remember_me', None): request.session.set_expiry(0)
        user = authenticate(username=request.POST.get('username', None), password=request.POST.get('password', None))
        if user is None: # Wrong credentials
            context = {'error': 'Wrong credentials!'}
        else: # Correct credentials
            context = None
        return auth_views.LoginView.as_view(template_name='login.html', extra_context = context)(request)
    else: # Get request -> load the page
        return render(request, 'login.html')

def signup(request, email=None):
    try:
        user = User.objects.get(username=email)
    except User.DoesNotExist:
        user = None
    if user is None:
        context = {'email':'New user {}'.format(email)}
        return render(request, 'signup.html', context=context)
    else:
        return render(request, 'login.html', {'email': email})