from django.shortcuts import render
from django.views.generic import ListView
from .models import S,B,Sest,M
# Create your views here.

class Schoollist(ListView):
    model = S
    model = B
class Directionlist(ListView):
    model = B
class Departmentlist(ListView):
    model = M
class Optionlist(ListView):
    model = Sest