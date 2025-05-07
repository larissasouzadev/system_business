from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
@login_required
def profile(request):
    # if request.user.is_staff:
    # verfifica se o user é admin ou não
        return render(request, 'base/profile.html')
        
def main(request):
    return render(request,'base/main.html')