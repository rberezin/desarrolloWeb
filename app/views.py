from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Player


def index(request):

    return render(request, 'index.html')


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Cuenta desactivada.")
        else:
            print "Datos invalidos: {0}, {1}".format(username, password)
            return HttpResponse("Datos invalidos")
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

