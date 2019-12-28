from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def main(request):
    if request.user.is_authenticated:
        render(request, 'mainPage.html')
    else:
        return render(request, 'welcome.html')
