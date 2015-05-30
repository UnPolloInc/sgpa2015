from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
import re
from proyectos.models import Proyecto
from roles.forms import RolForm, RolUpdateForm
from roles.models import Rol
from usuarios.models import Usuario


class CrearRol(CreateView):
    """
        *Vista Basada en Clase para crear proyectos*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear proyectos
            + *success_url*: url en caso de exito
    """
    template_name = 'roles/create.html'
    form_class = RolForm
    success_url = '/proyectos'

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CrearRol, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(CrearRol, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(CrearRol, self).get_form_kwargs(**kwargs)
        proyecto=Proyecto.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['proyecto'] = proyecto.pk
        return kwargs

    def get_success_url(self, **kwargs):
        kwargs = super(CrearRol, self).get_form_kwargs(**kwargs)
        return reverse('lista_rol',args=[self.kwargs['pk']])

class IndexView(ListView):
    """
        *Vista basada en Clase para lista de sprint*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'roles/rol_list'
    model = Rol

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['lider'] = self.request.user
        context['cliente'] = self.request.user
        return context

    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        return qs.filter(proyecto=self.kwargs['pk'])




class UpdateRol(UpdateView):
    """
        *Vista Basada en Clase para modificar un rol:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el sprint
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'roles/update.html'
    model = Rol
    form_class = RolUpdateForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateRol, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UpdateRol, self).get_context_data(**kwargs)
        sprint = Rol.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=sprint.proyecto.pk)
        return context


    def get_success_url(self, **kwargs):
        kwargs = super(UpdateRol, self).get_form_kwargs(**kwargs)
        sprint = Rol.objects.get(pk=self.kwargs['pk'])
        return reverse('lista_rol',args=[sprint.proyecto.pk])

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


@login_required
def search(request,pk):
    """
    :param request: request HTTP
    :return: retorna una lista de objetos que cumplan con el parametro de busqueda.
    """
    query_string = ''
    found_entries = None
    proyecto= None
    if ('busqueda' in request.GET) and request.GET['busqueda'].strip():
        query_string = request.GET['busqueda']
        entry_query = get_query(query_string, ['name'])
        found_entries = Rol.objects.filter(entry_query).order_by('name')
        proyecto = Proyecto.objects.get(pk=pk)
    return render_to_response('roles/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries, 'proyecto': proyecto },
                          context_instance=RequestContext(request))