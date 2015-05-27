from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from flujos.models import Flujos
from proyectos.models import Proyecto
from miembros.models import Miembro
from sprint.models import Sprint
from us.forms import usForm, usUpdateForm, PriorizarForm, usasigForm, registroForm
from usuarios.views import get_query
import re
from django.db.models import Q
from us.models import us, registroTrabajoUs


class Asignacion(UpdateView):
    """
        *Vista Basada en Clase para modificar un flujo:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'us/asignar.html'
    model = us
    form_class = usasigForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Asignacion, self).dispatch(*args, **kwargs)

    def get_success_url(self, **kwargs):
        kwargs = super(Asignacion, self).get_form_kwargs(**kwargs)
        US = us.objects.get(pk=self.kwargs['pk'])
        sprint = Sprint.objects.get(pk=US.sprint.pk)
        return reverse('lista_us',args=[sprint.proyecto.pk])

    def get_context_data(self, **kwargs):
        context = super(Asignacion, self).get_context_data(**kwargs)
        userstorie = us.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=userstorie.proyecto.pk)
        return context


    def get_form(self, form_class):
        form = super(Asignacion, self).get_form(form_class)
        userstorie = us.objects.get(pk=self.kwargs['pk'])
        form.fields['flujo'].queryset = Flujos.objects.filter(proyecto=userstorie.proyecto.pk)
        form.fields['sprint'].queryset = Sprint.objects.filter(proyecto=userstorie.proyecto.pk)
        form.fields['responsable'].queryset = Miembro.objects.filter(proyecto=userstorie.proyecto.pk)
        return form

class Createus(CreateView):
    """
        *Vista Basada en Clase para crear flujos*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear flujos
            + *success_url*: url en caso de exito
    """
    template_name = 'us/crear.html'
    form_class = usForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Createus, self).dispatch(*args, **kwargs)




    def get_form_kwargs(self, **kwargs):
        kwargs = super(Createus, self).get_form_kwargs(**kwargs)
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['proyecto'] = proyecto.pk
        return kwargs

    def get_success_url(self, **kwargs):
        kwargs = super(Createus, self).get_form_kwargs(**kwargs)
        return reverse('lista_us',args=[self.kwargs['pk']])

class IndexView(ListView):
    """
        *Vista basada en Clase para lista de flujos*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'us/us_list'
    model = us

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        userstories = us.objects.filter(proyecto=self.kwargs['pk'])
        return userstories.exclude(flujo__isnull=False, sprint__isnull=False, responsable__isnull=False)


class usMixin(object):
    """
        *Vista Basada en Clase para soporte de eliminacion de proyecto*:
            + *model*: modelo a ser eliminado
    """
    model = us

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Proyecto'})
        return kwargs



class Deleteus(usMixin, DeleteView):
    """
        *Vista Basada en Clase para eliminar flujos*:
            + *template_name*: nombre del template a ser rendirizado
            + *success_url: url a ser redireccionada en caso de exito*
    """
    template_name = 'us/delete_confirm.html'

    success_url = '/us'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Deleteus, self).dispatch(*args, **kwargs)



class Updateus(UpdateView):
    """
        *Vista Basada en Clase para modificar un flujo:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'us/update.html'
    model = us
    form_class = usUpdateForm
    #success_url = '/us'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Updateus, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Updateus, self).get_context_data(**kwargs)
        US = us.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=US.proyecto.pk)
        return context


    def get_success_url(self, **kwargs):
        kwargs = super(Updateus, self).get_form_kwargs(**kwargs)
        US = us.objects.get(pk=self.kwargs['pk'])
        return reverse('lista_us',args=[US.proyecto.pk])


class PriorizarUs(UpdateView):
    """
        *Vista Basada en Clase para modificar un flujo:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'us/update.html'
    model = us
    form_class = PriorizarForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PriorizarUs, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PriorizarUs, self).get_context_data(**kwargs)
        sprint = Sprint.objects.get(pk=self.kwargs['pk'])
        context['proyecto']= Proyecto.objects.get(pk=sprint.proyecto.pk)
        return context


    def get_success_url(self, **kwargs):
        kwargs = super(PriorizarUs, self).get_form_kwargs(**kwargs)
        US = us.objects.get(pk=self.kwargs['pk'])
        sprint = Sprint.objects.get(pk=US.sprint.pk)
        return reverse('lista_us',args=[sprint.proyecto.pk])


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

        found_entries = us.objects.filter(entry_query).order_by('nombre')
    return render_to_response('us/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))


class createRegistro(CreateView):

    """
        *Vista Basada en Clase para crear flujos*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear flujos
            + *success_url*: url en caso de exito
    """
    template_name = 'us/crearRegistro.html'
    form_class = registroForm
    #success_url = '/us'

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(createRegistro, self).dispatch(*args, **kwargs)

    #def get_family(self):
    #    return get_object_or_404(Family, pk=self.kwargs.get('family_pk'))


    def get_form_kwargs(self, **kwargs):
        kwargs = super(createRegistro, self).get_form_kwargs(**kwargs)
        #proyecto = Proyecto.objects.get(pk=self.kwargs['pk'])
        kwargs['initial']['us'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self, **kwargs):
        kwargs = super(createRegistro, self).get_form_kwargs(**kwargs)
        return reverse('lista_registro',args=[self.kwargs['proyecto'],self.kwargs['pk']])

class registroView(ListView):
    """
        *Vista basada en Clase para lista de flujos*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'us/lista_registro.html'
    model = registroTrabajoUs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(registroView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(registroView, self).get_context_data(**kwargs)
        #context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        #qs = super(registroView, self).get_queryset()
        registros = registroTrabajoUs.objects.filter(us=self.kwargs['pk'])
        return registros