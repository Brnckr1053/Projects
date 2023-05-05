from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Team, Player
from django.urls import reverse
from django.contrib.auth import login



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

@login_required
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'team_detail.html', {'team': team})

@login_required
def team_create(request):
    if request.method == 'POST':
        city = request.POST['city']
        mascot = request.POST['mascot']
        team = Team(city=city, mascot=mascot)
        team.save()
        return redirect('team_detail', pk=team.pk)
    else:
        return render(request, 'team_form.html')

@login_required
def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.city = request.POST['city']
        team.mascot = request.POST['mascot']
        team.save()
        return redirect('team_detail', pk=team.pk)
    else:
        return render(request, 'team_form.html', {'team': team})

@login_required
def player_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        team_ids = request.POST.getlist('team_ids')
        player = Player(first_name=first_name, last_name=last_name)
        player.save()
        player.teams.set(team_ids)
        return redirect('player_detail', pk=player.pk)
    else:
        teams = Team.objects.all()
        return render(request, 'player_form.html', {'teams': teams})

@login_required
def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'player_detail.html', {'player': player})

