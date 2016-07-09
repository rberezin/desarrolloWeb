from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Player, Match, Team
from django.db.models import Q
from operator import itemgetter


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


@login_required
def nextmatch(request):
    current = request.user
    player = Player.objects.get(user=current)
    team = player.team
    matchs = Match.objects.filter(Q(teaml=team) | Q(teamf=team))
    return render(request, 'matchs.html', {'matchs': matchs, 'team': team})


@login_required
def teaminfo(request):
    current = request.user
    player = Player.objects.get(user=current)
    team = player.team
    players = Player.objects.filter(team=team)
    return render(request, 'teaminfo.html', {'team': team, 'players': players})


@login_required
def userinfo(request):
    current = request.user
    player = Player.objects.get(user=current)
    return render(request, 'playerinfo.html', {'player': player})


@login_required
def tabla(request):
    current = request.user
    player = Player.objects.get(user=current)
    ligue = player.team.ligue
    teams = Team.objects.filter(ligue=ligue)
    tabla = []
    for team in teams:
        ganados = Match.objects.filter(ligue=ligue, win=team).count()
        empatados = Match.objects.filter(ligue=ligue, draw=True).count()
        perdidos = Match.objects.filter(ligue=ligue, lose=team).count()
        puntos = ganados*3 + empatados
        dato = [team.name, puntos, ganados, empatados, perdidos]
        tabla.append(dato)
    return render(request, 'tabla.html', {'tabla': tabla, 'ligue': ligue})
