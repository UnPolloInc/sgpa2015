from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from usuarios.forms import UserForm
from usuarios.models import Usuario

# Create your views here.


class IndexView(ListView):
    template_name = 'usuario_list'
    model = Usuario

class CreateUser(CreateView):
    template_name = 'usuarios/create.html'
    form_class = UserForm
    success_url = '/'

