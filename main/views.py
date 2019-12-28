from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def main(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        return render(request, 'welcome.html')

@login_required
def main_page(request):
    return render(request, 'main_page.html')
