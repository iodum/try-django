from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Treasure
from django.contrib.auth.models import User
from .forms import TreasureForm


def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, 'index.html', {'treasures': treasures, 'form': form})


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})


def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        treasure = form.save(commit=False)
        treasure.user = request.user
        treasure.save()

    return HttpResponseRedirect('/')


def profile(request, username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'treasures': treasures})
