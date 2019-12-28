from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def main(request):
    if request.user.is_authenticated:
        return mainPage(request)
    else:
        return render(request, 'welcome.html')

@login_required
def mainPage(request):
    return render(request, 'mainPage.html')
