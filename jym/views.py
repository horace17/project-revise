from django.shortcuts import render
from .models import Team
from . serializers import TeamSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
    teams = Team.objects.all()
    return render(request, 'index.html',{'teams':teams})

class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


