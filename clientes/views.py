from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from clientes.forms import UserForm,UserUpdateForm
from clientes.models import Cliente
from django.utils.decorators import method_decorator
import re
from django.db.models import Q


class IndexView(ListView):
    """
        *Vista basada en Clase para lista de clientes*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'cliente_list'
    model = Cliente
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class CreateUser(CreateView):
    """
        *Vista Basada en Clase para crear clientes*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear clientes
            + *success_url*: url en caso de exito
    """
    template_name = 'clientes/create.html'
    form_class = UserForm
    success_url = '/clientes'

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateUser, self).dispatch(*args, **kwargs)

class UserMixin(object):
    """
        *Vista Basada en Clase para soporte de eliminacion de clientes*:
            + *model*: modelo a ser eliminado
    """
    model = Cliente

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Cliente'})
        return kwargs



class DeleteUser(UserMixin, DeleteView):
    """
        *Vista Basada en Clase para eliminar clientes*:
            + *template_name*: nombre del template a ser rendirizado
            + *success_url: url a ser redireccionada en caso de exito*
    """
    template_name = 'clientes/delete_confirm.html'

    success_url = '/clientes'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteUser, self).dispatch(*args, **kwargs)

class UpdateUser(UpdateView):
    """
        *Vista Basada en Clase para modificar un clientes:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el clientes
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'clientes/update.html'
    model = Cliente
    form_class = UserUpdateForm
    success_url = '/clientes/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateUser, self).dispatch(*args, **kwargs)


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

        entry_query = get_query(query_string, ['username','first_name', 'last_name'])

        found_entries = Cliente.objects.filter(entry_query).order_by('username')
    return render_to_response('clientes/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))