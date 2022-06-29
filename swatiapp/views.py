from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DynamicSerializer
# Create your views here.
from .models import Dynamic
from django.core import serializers
from django.forms.models import model_to_dict




from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")


def cause(request):
    return render(request, "causes.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def team(request):
    return render(request, "team.html")


def blog(request):
    dynamic = Dynamic.objects.all()
    return render(request, "blog.html",{"dynamic":dynamic})


class DynamicViewSet(viewsets.ModelViewSet):
    queryset = Dynamic.objects.all().order_by('number')
    serializer_class = DynamicSerializer
