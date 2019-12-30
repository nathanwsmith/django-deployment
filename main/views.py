from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def welcome(request):
    if request.user.is_authenticated: #loged in user
        return mainPage(request) #?
    else: # not logged in user
        if request.method == 'GET':
            email = request.GET.get('email', None)
            if email is not None: # pushed button sign-up
                try:
                    user = User.objects.get(username=request.GET.get('email', None))
                except User.DoesNotExist:
                    user = None
                if user is None: #new user -> redirect to signup with parameter email
                    if email == '':
                        return redirect('signup')
                    else:
                        return redirect(reverse('signup') + '?email=' + email)
                else: #existing user -> redirect with query parameter email
                    return redirect(reverse('login') + '?email=' + email)
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
            context = {'error' : 'Wrong credentials!', 'email' : request.POST.get('username', None)}
        else: # Correct credentials
            context = None
        return auth_views.LoginView.as_view(template_name='login.html', extra_context = context)(request)
    else: # Get request -> load the page
        email = request.GET.get('email', None)
        if email is None:
            return render(request, 'login.html')
        else:
            return render(request, 'login.html', {'email': email})

def signup(request):
    if request.method == 'POST': # button register
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        #Form validation ???
        if (email is not None) and (password is not None) and (password2 is not None): #non-blank fields
            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                user = None
            if user is None:#check if user is already exists in DB
                if password == password2: #equal passwords
                    user = User.objects.create_user(email, email, password)
                    user.save()
                    auth_login(request, user)
                    return redirect('welcome')
                else:#not equal passwords
                    context = {'email': email, 'message': 'Passwords are not the same, try again!'}
                    return render(request, 'signup.html', context=context)
            else:#existing user
                context = {'email': email, 'message': 'Existing user, try with another e-mail'}
                return render(request, 'signup.html', context=context)
        else:#some of the fields are blank
            context = {'email':email, 'message':'Try again'}
            return render(request, 'signup.html', context=context)
    else: #GET
        email=request.GET.get('email', None)
        if email is None: #blank email
            return render(request, 'signup.html')
        else: #filled in email
            context = {'email':email}
            return render(request, 'signup.html', context=context)
