from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import request
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from clientes.models import Cliente
from mensajes.forms import mensajesForm, mensajesUpdateForm
from mensajes.models import Mensaje
import re
from django.db.models import Q
from proyectos.models import Proyecto
from usuarios.models import Usuario
from miembros.models import Miembro

class CreateMensaje(CreateView):
    """
        *Vista Basada en Clase para crear proyectos*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear proyectos
            + *success_url*: url en caso de exito
    """

    template_name = 'mensajes/create.html'
    form_class = mensajesForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateMensaje, self).dispatch(*args, **kwargs)


    def get_form(self, form_class):
        form = super(CreateMensaje, self).get_form(form_class)
        form.fields['destinatario'].queryset = Miembro.objects.filter(proyecto=self.kwargs['pk'])
        return form


    def get_form_kwargs(self, **kwargs):
        kwargs = super(CreateMensaje, self).get_form_kwargs(**kwargs)
        usuario=Usuario.objects.get(pk=self.kwargs['usuario'])
        kwargs['initial']['remitente'] = usuario.pk
        kwargs['initial']['proyecto'] = Proyecto.objects.get(pk=self.kwargs['pk'])
        return kwargs


    def get_success_url(self, **kwargs):
        kwargs = super(CreateMensaje, self).get_form_kwargs(**kwargs)
        return reverse('lista_recibidos',args=[self.kwargs['pk']])




class EnviadosView(ListView):
    """
        *Vista basada en Clase para lista de mensajes*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'mensajes/mensajes_list.html'
    model = Mensaje

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EnviadosView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EnviadosView, self).get_context_data(**kwargs)
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

    def get_queryset(self):
        qs=super(EnviadosView, self).get_queryset()
        return qs.filter(proyecto=self.kwargs['pk']).filter(remitente=self.request.user)



class MensajeMixin(object):
    """
        *Vista Basada en Clase para soporte de eliminacion de proyecto*:
            + *model*: modelo a ser eliminado
    """
    model = Mensaje

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'mensajes'})
        return kwargs



class DeleteMensaje(MensajeMixin, DeleteView):
    """
        *Vista Basada en Clase para eliminar proyectos*:
            + *template_name*: nombre del template a ser rendirizado
            + *success_url: url a ser redireccionada en caso de exito*
    """
    template_name = 'mensajes/delete_confirm.html'

    #success_url = '/proyectos/flujos/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteMensaje, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DeleteMensaje, self).get_context_data(**kwargs)
        mensaje = Mensaje.objects.get(pk=self.kwargs['pk'])
        context['mensaje'] = mensaje
        context['proyecto'] = mensaje.proyecto
        return context

    def get_success_url(self, **kwargs):
        kwargs = super(DeleteMensaje, self).get_context_data(**kwargs)
        mensaje = Mensaje.objects.get(pk=self.kwargs['pk'])
        proyecto = mensaje.proyecto.pk
        return reverse('lista_recibidos', args=[proyecto])



#class UpdateMensaje(UpdateView):
    """
        *Vista Basada en Clase para modificar un proyecto:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
#    template_name = 'mensajes/update.html'
#    model = mensajes
#    form_class = mensajesUpdateForm
#    success_url = '/mensajes/'

#    @method_decorator(login_required)
#    def dispatch(self, *args, **kwargs):
#        return super(UpdateMensaje, self).dispatch(*args, **kwargs)

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

        entry_query = get_query(query_string, ['destinatario'])

        found_entries = Mensaje.objects.filter(entry_query).order_by('destinatario')
    return render_to_response('mensajes/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))



class RecibidosView(ListView):
    """
        *Vista basada en Clase para lista de mensajes*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'mensajes/mensajes_list.html'
    model = Mensaje

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecibidosView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RecibidosView, self).get_context_data(**kwargs)
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

    def get_queryset(self):
        qs=super(RecibidosView, self).get_queryset()
        miembro = Miembro.objects.filter(proyecto=self.kwargs['pk']).filter(usuario=self.request.user)
        return qs.filter(proyecto=self.kwargs['pk']).filter(destinatario=miembro)
