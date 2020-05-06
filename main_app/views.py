from django.shortcuts import render
from .models import Finch
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class FinchList(ListView):
    model = Finch

    def get_queryset(self):
        return Finch.objects.all()

class FinchDetail(DetailView):
    model = Finch