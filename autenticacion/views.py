from django.shortcuts import render, render_to_response

# Create your views here.

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='/login')
def index(request):
    #logout(request)
    #return redirect('principal')
    #return HttpResponse("You found my secret place!")
    return render_to_response('main/principal.html')

def principal(request):
    return HttpResponse("ola que ase!")

def logout_view(request):
        logout(request)
        return redirect('/login/?next=%s')

# Redirect to a success page.