from django.shortcuts import render
from .models import Finch
from django.views.generic import ListView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class FinchList(ListView):
    model = Finch

    def get_queryset(self):
        return Finch.objects.all()


def finches_detail (request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch' : finch })