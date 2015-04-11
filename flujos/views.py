from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from flujos.forms import FlujosForm, FlujosUpdateForm
from flujos.models import Flujos
from usuarios.views import get_query
import re
from django.db.models import Q


class CreateFlujos(CreateView):
    """
        *Vista Basada en Clase para crear flujos*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear flujos
            + *success_url*: url en caso de exito
    """
    template_name = 'flujos/crear.html'
    form_class = FlujosForm
    success_url = '/flujos'

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateFlujos, self).dispatch(*args, **kwargs)

class IndexView(ListView):
    """
        *Vista basada en Clase para lista de flujos*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'flujos/flujos_list'
    model = Flujos

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

class FlujosMixin(object):
    """
        *Vista Basada en Clase para soporte de eliminacion de proyecto*:
            + *model*: modelo a ser eliminado
    """
    model = Flujos

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Proyecto'})
        return kwargs



class DeleteFlujos(FlujosMixin, DeleteView):
    """
        *Vista Basada en Clase para eliminar flujos*:
            + *template_name*: nombre del template a ser rendirizado
            + *success_url: url a ser redireccionada en caso de exito*
    """
    template_name = 'flujos/delete_confirm.html'

    success_url = '/flujos'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteFlujos, self).dispatch(*args, **kwargs)


class UpdateFlujos(UpdateView):
    """
        *Vista Basada en Clase para modificar un flujo:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'flujos/update.html'
    model = Flujos
    form_class = FlujosUpdateForm
    success_url = '/flujos'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateFlujos, self).dispatch(*args, **kwargs)

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

        found_entries = Flujos.objects.filter(entry_query).order_by('nombre')
    return render_to_response('flujos/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))