from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from sprint.forms import SprintForm, SprintUpdateForm
from sprint.models import Sprint
from usuarios.views import get_query
import re
from django.db.models import Q


class CreateSprint(CreateView):
    """
        *Vista Basada en Clase para crear sprint*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear sprint
            + *success_url*: url en caso de exito
    """
    template_name = 'sprint/create.html'
    form_class = SprintForm
    success_url = '/sprint'

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateSprint, self).dispatch(*args, **kwargs)

class IndexView(ListView):
    """
        *Vista basada en Clase para lista de sprint*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'sprint/sprint_list'
    model = Sprint

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    """
    def get_queryset(self):
        lideres = Sprint.objects.filter(lider_proyecto=self.request.user)
        clientes = Sprint.objects.filter( cliente=self.request.user)
        if lideres:
            return lideres
        elif clientes:
            return clientes
        elif self.request.user.is_superuser:
            return Sprint.objects.all()
        else:
            return lideres

    """


class SprintMixin(object):
    """
        *Vista Basada en Clase para soporte de eliminacion de sprint*:
            + *model*: modelo a ser eliminado
    """
    model = Sprint

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Sprint'})
        return kwargs


"""
class DeleteSprint(SprintMixin, DeleteView):

        #*Vista Basada en Clase para eliminar sprint*:
         #   + *template_name*: nombre del template a ser rendirizado
          #  + *success_url: url a ser redireccionada en caso de exito*

    template_name = 'sprint/delete_confirm.html'

    success_url = '/sprint'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteSprint, self).dispatch(*args, **kwargs)

"""
class UpdateSprint(UpdateView):
    """
        *Vista Basada en Clase para modificar un sprint:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'sprint/update.html'
    model = Sprint
    form_class = SprintUpdateForm
    success_url = '/sprint/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateSprint, self).dispatch(*args, **kwargs)

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
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
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
def search(request):
    """
    :param request: request HTTP
    :return: retorna una lista de objetos que cumplan con el parametro de busqueda.
    """
    query_string = ''
    found_entries = None
    if ('busqueda' in request.GET) and request.GET['busqueda'].strip():
        query_string = request.GET['busqueda']

        entry_query = get_query(query_string, ['nombre'])

        found_entries = Sprint.objects.filter(entry_query).order_by('nombre')
    return render_to_response('sprint/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))