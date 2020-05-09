from django.shortcuts import render, redirect
from .models import Finch
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

    
@login_required
def finches_index(request):
  finches = Finch.objects.filter(user=request.user)
  return render(request, 'main_app/finch_list.html', { 'finches': finches })


class FinchDetail(LoginRequiredMixin, DetailView):
    model = Finch

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'description', 'age'] 


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

    

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('finches_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)