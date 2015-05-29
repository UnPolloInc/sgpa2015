from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from flujos.forms import FlujosForm, FlujosUpdateForm, ActividadForm
from flujos.models import Flujos, Actividad
from proyectos.models import Proyecto
from us.models import us
from usuarios.models import Usuario
from usuarios.views import get_query
import re
from django.db.models import Q

class IndexViewUsfl(ListView):
    """
        *Vista basada en Clase para lista de sprint*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'flujos/us_list.html'
    model = us

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexViewUsfl, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexViewUsfl, self).get_context_data(**kwargs)
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['proyecto'] = proyecto
        context['lider'] = Usuario.objects.get(pk=proyecto.lider_proyecto)
        return context

    def get_queryset(self):
        qs = super(IndexViewUsfl,self).get_queryset()
        userstories = us.objects.filter(flujo=self.kwargs['flujo'])
        return userstories

class CreateFlujos(CreateView):
    """
        *Vista Basada en Clase para crear flujos*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear flujos
            + *success_url*: url en caso de exito
    """
    template_name = 'flujos/crear.html'
    form_class = FlujosForm

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateFlujos, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(CreateFlujos, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        return context
    def get_form_kwargs(self, **kwargs):
        kwargs = super(CreateFlujos, self).get_form_kwargs(**kwargs)

        proyecto=Proyecto.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['proyecto'] = proyecto.pk
        return kwargs

    def get_success_url(self, **kwargs):
        kwargs = super(CreateFlujos, self).get_form_kwargs(**kwargs)
        return reverse('lista_flujo',args=[self.kwargs['pk']])

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

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['proyecto'] = proyecto
        context['lider'] = Usuario.objects.get(pk=self.request.user)

        return context

    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        return qs.filter(proyecto=self.kwargs['pk'])

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

    success_url = '/flujos/configurar/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteFlujos, self).dispatch(*args, **kwargs)
"""
    def get_context_data(self, **kwargs):
        context = super(DeleteFlujos, self).get_context_data(**kwargs)
        flujo = Flujos.objects.get(pk=self.kwargs['pk'])
        context['flujo'] = flujo
        context['proyecto'] = Proyecto.objects.get(pk=flujo.proyecto.pk)
        return context
"""
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateFlujos, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UpdateFlujos, self).get_context_data(**kwargs)
        flujo = Flujos.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=flujo.proyecto.pk)
        return context


    def get_success_url(self, **kwargs):
        kwargs = super(UpdateFlujos, self).get_form_kwargs(**kwargs)
        flujo = Flujos.objects.get(pk=self.kwargs['pk'])
        return reverse('lista_flujo', args=[flujo.proyecto.pk])

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
def search(request, pk):
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
        proyecto = Proyecto.objects.get(pk=pk)
    return render_to_response('flujos/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries, 'proyecto':proyecto },
                          context_instance=RequestContext(request))

class CreateActividad(CreateView):
    """
        *Vista Basada en Clase para crear flujos*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear flujos
            + *success_url*: url en caso de exito
    """
    template_name = 'actividades/crear.html'
    form_class = ActividadForm

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateActividad, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(CreateActividad, self).get_context_data(**kwargs)
        context['flujo'] = Flujos.objects.get(pk=self.kwargs['pk'])
        flujo=Flujos.objects.get(pk=self.kwargs['pk'])
        context['proyecto'] = Proyecto.objects.get(pk=flujo.proyecto.pk)
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(CreateActividad, self).get_form_kwargs(**kwargs)

        flujo=Flujos.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['flujo'] = flujo.pk
        return kwargs

    def get_success_url(self, **kwargs):
        kwargs = super(CreateActividad, self).get_form_kwargs(**kwargs)
        flujo=Flujos.objects.get(pk=self.kwargs['pk'])
        return reverse('lista_actividad',args=[flujo.pk])

class ActividadesListView(ListView):
    """
        *Vista basada en Clase para lista de flujos*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'actividades/actividades_list.html'

    model = Actividad

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ActividadesListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ActividadesListView, self).get_context_data(**kwargs)
        context['flujo'] = Flujos.objects.get(pk=self.kwargs['pk'])
        flujo = Flujos.objects.get(pk=self.kwargs['pk'])
        context['proyecto'] = Proyecto.objects.get(pk=flujo.proyecto.pk)
        context['us_list'] = us.objects.filter(flujo=flujo)
        return context

    def get_queryset(self):
        qs = super(ActividadesListView, self).get_queryset()
        return qs.filter(flujo=self.kwargs['pk'])

