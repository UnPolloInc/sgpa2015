from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from clientes.models import Cliente
from miembros.forms import MiembroForm, MiembroUpdateForm
from miembros.models import Miembro
from django.utils.decorators import method_decorator
import re
from django.db.models import Q, ProtectedError
from roles.models import Rol
from usuarios.models import Usuario
from proyectos.models import Proyecto
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from usuarios.views import get_query





class IndexViewVerUser(ListView):
    """
        *Vista basada en Clase para lista de usuarios*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    model = Usuario
    template_name = 'miembros/usuarios_list.html'


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexViewVerUser, self).dispatch(*args, **kwargs)


    def get_queryset(self):
        qs = super(IndexViewVerUser,self).get_queryset()
        miembros = Miembro.objects.filter(proyecto=self.kwargs['pk'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk'])
        qs = Usuario.objects.all()
        return qs.exclude(id__in=[miembro.usuario.pk for miembro in miembros]).exclude(pk=proyecto.pk).exclude(pk = proyecto.lider_proyecto)

    def get_context_data(self, **kwargs):
        context = super(IndexViewVerUser, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        try:
            context['lider'] = Usuario.objects.get(pk=self.request.user)
        except:
            context['lider'] = None

        try:
            context['cliente'] = Cliente.objects.get(pk = self.request.user)
        except:
            context['cliente'] = None
        return context




class CreateMiembro(CreateView):
    """
        *Vista Basada en Clase para crear clientes*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear clientes
            + *success_url*: url en caso de exito
    """
    template_name = 'miembros/create.html'
    form_class = MiembroForm
    #success_url = '/miembros'

    # @user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateMiembro, self).dispatch(*args, **kwargs)

    '''def get_context_data(self, **kwargs):
        context = super(CreateMiembro, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['usuario'] = Usuario.objects.get(pk=self.kwargs['usuario'])
        return context'''

    def get_form_kwargs(self, **kwargs):
        kwargs = super(CreateMiembro, self).get_form_kwargs(**kwargs)
        proyecto=Proyecto.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['proyecto'] = proyecto.pk
        usuario=Usuario.objects.get(pk=self.kwargs['usuario'])
        kwargs['initial']['usuario'] = usuario.pk
        kwargs.update({'proyecto': proyecto})

        return kwargs

    def get_success_url(self, **kwargs):
        kwargs = super(CreateMiembro, self).get_form_kwargs(**kwargs)
        return reverse('miembros_listar',args=[self.kwargs['pk']])

class IndexView(ListView):
    """
        *Vista basada en Clase para lista de clientes*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'miembros/miembros_list.html'
    model = Miembro

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['proyecto'] = proyecto
        try:
            context['lider'] = Usuario.objects.get(pk=self.request.user)
        except:
            context['lider'] = None

        try:
            context['cliente'] = Cliente.objects.get(pk = self.request.user)
        except:
            context['cliente'] = None
        return context

    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        proyecto=Proyecto.objects.get(pk=self.kwargs['pk'])
        return qs.filter(proyecto=proyecto).exclude(usuario=proyecto.lider_proyecto)


class MiembroMixin(object):
    """
        *Vista Basada en Clase para soporte de eliminacion de clientes*:
            + *model*: modelo a ser eliminado
    """
    model = Miembro
    def get_context_data(self, **kwargs):
        context = super(MiembroMixin, self).get_context_data(**kwargs)
        miembro = Miembro.objects.get(pk=self.kwargs['pk'])
        context['miembro'] = miembro
        context['proyecto'] = Proyecto.objects.get(pk=miembro.proyecto.pk)
        return context

"""
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'miembro'})
        return kwargs
"""

class DeleteMiembro(MiembroMixin, DeleteView):
    """
        *Vista Basada en Clase para eliminar clientes*:
            + *template_name*: nombre del template a ser rendirizado
            + *success_url: url a ser redireccionada en caso de exito*
    """
    template_name = 'miembros/delete_confirm.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteMiembro, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DeleteMiembro, self).get_context_data(**kwargs)
        miembro = Miembro.objects.get(pk=self.kwargs['pk'])
        context['miembro'] = Miembro
        context['proyecto'] = Proyecto.objects.get(pk=miembro.proyecto.pk)
        return context

    def delete(self, *args, **kwargs):
        try:
            return super(DeleteMiembro, self).delete(
                self, *args, **kwargs
            )
        except ProtectedError as e:
            # Return the appropriate response
            #return HttpResponseForbidden()
            kwargs = super(DeleteMiembro, self).get_context_data(**kwargs)
            miembro = Miembro.objects.get(pk=self.kwargs['pk'])
            url = reverse('miembros_listar', kwargs={'pk':miembro.proyecto.pk})
            return HttpResponseRedirect(url)
            #
            #return reverse('miembros_listar',args=[miembro.proyecto.pk])


    def get_success_url(self, **kwargs):
        kwargs = super(DeleteMiembro, self).get_context_data(**kwargs)
        miembro = Miembro.objects.get(pk=self.kwargs['pk'])
        return reverse('miembros_listar',args=[miembro.proyecto.pk])

class UpdateMiembro(UpdateView):
    """
        *Vista Basada en Clase para modificar un clientes:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el clientes
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'miembros/update.html'
    model = Miembro
    form_class = MiembroUpdateForm
    success_url = '/miembros'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateMiembro, self).dispatch(*args, **kwargs)


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """
    Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']


    :param query_string: cadena completa de busqueda
    :param findterms: expresion regular para encontrar las palabras
    :param normspace: expresion regular para normalizar el espacio
    :return: una lista de palabras separadas y normalizadas
    """

    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    """

    :param query_string: Cadena que se va usar para la busqueda.
    :param search_fields: Campos que se usan para comparar con la cadena de busqueda.
    :return: Retorna una lista, que es una combinacion de objetos Q que cumplen con
    la cadena de busqueda parcial o totalmente.

    """
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


@login_required
def search(request, pk):
    """
    :param request: request HTTP
    :return: retorna una lista de objetos que cumplan con el parametro de busqueda.
    """
    query_string = ''
    found_entries = None
    if ('busqueda' in request.GET) and request.GET['busqueda'].strip():
        query_string = request.GET['busqueda']


        entry_query = get_query(query_string, ['username'])
        proyecto = Proyecto.objects.get(pk=pk)
        found_entries = Miembro.objects.filter().filter(proyecto=proyecto).order_by('username')

    return render_to_response('miembros/search_results.html',
                              {'query_string': query_string, 'found_entries': found_entries, 'proyecto':proyecto},
                              context_instance=RequestContext(request))



