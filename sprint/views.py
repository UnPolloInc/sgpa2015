from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import request
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from flujos.models import Flujos
from miembros.models import Miembro
from proyectos.models import Proyecto
from sprint.forms import SprintForm, SprintUpdateForm, usUpdateForm, EjecutarSprintForm, FinalizarSprintForm
from sprint.models import Sprint, Estado
from usuarios.models import Usuario
from usuarios.views import get_query
import re
from django.db.models import Q
from us.models import us

class IndexViewFinalizado(ListView):
    """
        *Vista basada en Clase para lista de sprint*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'sprint/finalizado.html'
    model = Sprint

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexViewFinalizado, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexViewFinalizado, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['lider'] = Usuario.objects.get(pk=self.request.user)
        return context

    def get_queryset(self):
        qs = super(IndexViewFinalizado,self).get_queryset()
        sprint = Sprint.objects.filter(proyecto=self.kwargs['pk'])
        sp = sprint.filter(estado = 3)
        return sp



class IndexViewEnEjecucion(ListView):
    """
        *Vista basada en Clase para lista de sprint*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'sprint/finalizar_sprint_list.html'
    model = Sprint

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexViewEnEjecucion, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexViewEnEjecucion, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['lider'] = Usuario.objects.get(pk=self.request.user)
        return context

    def get_queryset(self):
        qs = super(IndexViewEnEjecucion,self).get_queryset()
        sprint = Sprint.objects.filter(proyecto=self.kwargs['pk'])
        sp = sprint.filter(estado = 2)
        return sp


class FinalizarSprint(UpdateView):
    """
        *Vista Basada en Clase para modificar un sprint:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'sprint/finalizar_confirm.html'
    model = Sprint
    form_class = FinalizarSprintForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FinalizarSprint, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        kwargs = super(FinalizarSprint, self).get_form_kwargs(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['estado'] = sprint.estado.pk=3
        return kwargs


    def get_context_data(self, **kwargs):
        context = super(FinalizarSprint, self).get_context_data(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=sprint.proyecto.pk)
        context['lider'] = Usuario.objects.get(pk=self.request.user)
        return context


    def get_success_url(self, **kwargs):
        kwargs = super(FinalizarSprint, self).get_form_kwargs(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        return reverse('lista_sprint',args=[sprint.proyecto.pk])


class EjecutarSprint(UpdateView):
    """
        *Vista Basada en Clase para modificar un sprint:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'sprint/ejecutar_sprint.html'
    model = Sprint
    form_class = EjecutarSprintForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EjecutarSprint, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        kwargs = super(EjecutarSprint, self).get_form_kwargs(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['estado'] = sprint.estado.pk=2
        return kwargs


    def get_context_data(self, **kwargs):
        context = super(EjecutarSprint, self).get_context_data(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=sprint.proyecto.pk)
        context['lider'] = Usuario.objects.get(pk=self.request.user)
        return context


    def get_success_url(self, **kwargs):
        kwargs = super(EjecutarSprint, self).get_form_kwargs(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        return reverse('lista_sprint',args=[sprint.proyecto.pk])

class ReasignarUs(UpdateView):
    """
        *Vista Basada en Clase para modificar un sprint:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'sprint/updateus.html'
    model = us
    form_class = usUpdateForm


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReasignarUs, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ReasignarUs, self).get_context_data(**kwargs)
        userstorie = us.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=userstorie.proyecto.pk)
        return context

    def get_form(self, form_class):
        form = super(ReasignarUs, self).get_form(form_class)
        userstorie = us.objects.get(pk=self.kwargs['pk'])
        form.fields['flujo'].queryset = Flujos.objects.filter(proyecto=userstorie.proyecto.pk)
        form.fields['sprint'].queryset = Sprint.objects.filter(proyecto=userstorie.proyecto.pk)
        form.fields['responsable'].queryset = Miembro.objects.filter(proyecto=userstorie.proyecto.pk)
        return form

    def get_success_url(self, **kwargs):
        kwargs = super(ReasignarUs, self).get_form_kwargs(**kwargs)
        US = us.objects.get(pk=self.kwargs['pk'])
        return reverse('us_listar',args=[US.proyecto.pk, US.sprint.pk])


class IndexViewUs(ListView):
    """
        *Vista basada en Clase para lista de sprint*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'sprint/us_list.html'
    model = us

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexViewUs, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexViewUs, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        qs = super(IndexViewUs,self).get_queryset()
        userstories = us.objects.filter(sprint=self.kwargs['sprint'])
        return userstories

class CreateSprint(CreateView):
    """
        *Vista Basada en Clase para crear sprint*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear sprint
            + *success_url*: url en caso de exito
    """
    template_name = 'sprint/create.html'
    form_class = SprintForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateSprint, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateSprint, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(CreateSprint, self).get_form_kwargs(**kwargs)
        proyecto=Proyecto.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['proyecto'] = proyecto.pk
        kwargs['initial']['estado'] = 1
        return kwargs

    def get_success_url(self, **kwargs):
        kwargs = super(CreateSprint, self).get_form_kwargs(**kwargs)
        return reverse('lista_sprint',args=[self.kwargs['pk']])

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

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['lider'] = Usuario.objects.get(pk=self.request.user)
        return context

    def get_queryset(self):
        qs = super(IndexView,self).get_queryset()
        sprint = Sprint.objects.filter(proyecto=self.kwargs['pk'])
        sp = sprint.filter(estado = 1)
        return sp

class SprintMixin(object):
    """
        *Vista Basada en Clase para soporte de eliminacion de sprint*:
            + *model*: modelo a ser eliminado
    """
    model = Sprint

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Sprint'})
        return kwargs



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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateSprint, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UpdateSprint, self).get_context_data(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=sprint.proyecto.pk)
        return context


    def get_success_url(self, **kwargs):
        kwargs = super(UpdateSprint, self).get_form_kwargs(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        return reverse('lista_sprint',args=[sprint.proyecto.pk])

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
        entry_query = get_query(query_string, ['nombre'])
        found_entries = Sprint.objects.filter(entry_query).order_by('nombre')
        proyecto = Proyecto.objects.get(pk=pk)
    return render_to_response('sprint/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries, 'proyecto': proyecto },
                          context_instance=RequestContext(request))