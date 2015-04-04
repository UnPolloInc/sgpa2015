from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from proyectos.forms import ProyectoForm
from proyectos.models import Proyecto

class CreateProyecto(CreateView):
    """
        *Vista Basada en Clase para crear usuarios*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear usuarios
            + *success_url*: url en caso de exito
    """
    template_name = 'proyectos/create.html'
    form_class = ProyectoForm
    success_url = '/proyectos'

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateProyecto, self).dispatch(*args, **kwargs)

class IndexView(ListView):
    """
        *Vista basada en Clase para lista de usuarios*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'proyecto_list'
    model = Proyecto

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
