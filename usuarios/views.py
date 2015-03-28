from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import ListView,CreateView, DeleteView
from usuarios.forms import UserForm
from usuarios.models import Usuario
from django.utils.decorators import method_decorator
# Create your views here.


class IndexView(ListView):
    template_name = 'usuario_list'
    model = Usuario

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

class CreateUser(CreateView):
    template_name = 'usuarios/create.html'
    form_class = UserForm
    success_url = '/usuarios'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateUser, self).dispatch(*args, **kwargs)

class UserMixin(object):
    model = Usuario

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Usuario'})
        return kwargs

class DeleteUser(UserMixin, DeleteView):
    template_name = 'usuarios/delete_confirm.html'

    success_url = '/usuarios'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteUser, self).dispatch(*args, **kwargs)