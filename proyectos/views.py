from itertools import chain
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.legends import LineLegend
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.lineplots import GridLinePlot
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.colors import Color
from reportlab.graphics.widgets.markers import makeMarker
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import request
from django.shortcuts import render, render_to_response, get_object_or_404
from reportlab.graphics.charts.linecharts import HorizontalLineChart
# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from clientes.models import Cliente
from flujos.models import Flujos, Actividad
from miembros.models import Miembro
from proyectos.forms import ProyectoForm, ProyectoUpdateForm, ProyectoIniciarForm
from proyectos.models import Proyecto
from sprint.models import Sprint
from us.models import us, registroTrabajoUs
from usuarios.models import Usuario
from usuarios.views import get_query
import re
from django.db.models import Q
import datetime


class CreateProyecto(CreateView):
    """
        *Vista Basada en Clase para crear proyectos*:
            + *template_name*: nombre del template que vamos renderizar
            + *form_class*: formulario para crear proyectos
            + *success_url*: url en caso de exito
    """
    template_name = 'proyectos/create.html'
    form_class = ProyectoForm
    success_url = '/proyectos'

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateProyecto, self).dispatch(*args, **kwargs)

class IndexView(ListView):
    """
        *Vista basada en Clase para lista de proyectos*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'proyecto_list'
    model = Proyecto

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        lideres = Proyecto.objects.filter(lider_proyecto=self.request.user)
        clientes = Proyecto.objects.filter(cliente=self.request.user)
        miembros = Miembro.objects.filter(usuario=self.request.user)
        qs = Proyecto.objects.all()

        if self.request.user.is_superuser:
            return Proyecto.objects.all()
        else:
            matches = lideres | clientes | qs.filter(id__in=[miembro.proyecto.pk for miembro in miembros])
            return matches


class ProyectoMixin(object):
    """
        *Vista Basada en Clase para soporte de eliminacion de proyecto*:
            + *model*: modelo a ser eliminado
    """
    model = Proyecto

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Proyecto'})
        return kwargs



class ConfigurarProyecto(ProyectoMixin, DeleteView):
    """
        *Vista Basada en Clase para eliminar proyectos*:
            + *template_name*: nombre del template a ser rendirizado
            + *success_url: url a ser redireccionada en caso de exito*
    """
    template_name = 'main/menu.html'

    #success_url = '/proyectos/flujos/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ConfigurarProyecto, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConfigurarProyecto, self).get_context_data(**kwargs)
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


class UpdateProyecto(UpdateView):
    """
        *Vista Basada en Clase para modificar un proyecto:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'proyectos/update.html'
    model = Proyecto
    form_class = ProyectoUpdateForm
    success_url = '/proyectos/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateProyecto, self).dispatch(*args, **kwargs)



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

        found_entries = Proyecto.objects.filter(entry_query).order_by('nombre')
    return render_to_response('proyectos/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))


class Kanban(ListView):
    """
        *Vista basada en Clase para lista de sprint*:
            + *template_name*: nombre del template que vamos a renderizar
            + *model*: modelo que vamos a listar.
    """
    template_name = 'proyectos/kanban.html'
    model = Flujos

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Kanban, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Kanban, self).get_context_data(**kwargs)
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk'])
        context['proyecto'] = proyecto
        context['us_list'] = us.objects.filter(proyecto=proyecto).order_by('pk').exclude(estado_de_aprobacion='CAN')
        flujos= Flujos.objects.filter(proyecto=proyecto)

        context['actividades'] = Actividad.objects.filter(flujo__in = flujos ).order_by('pk')

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
        qs = super(Kanban,self).get_queryset()
        flujos = Flujos.objects.filter(proyecto=self.kwargs['pk']).order_by('pk')
        return flujos

class IniciarProyecto(UpdateView):
    """
        *Vista Basada en Clase para iniciar un proyecto:*
            +*template_name*: template a ser renderizado
            +*model*: modelo que se va modificar
            +*form_class*:Formulario para actualizar el usuario
            +*success_url*: url a ser redireccionada en caso de exito
    """
    template_name = 'proyectos/iniciar.html'
    model = Proyecto
    form_class = ProyectoIniciarForm
    #success_url = '/proyectos/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IniciarProyecto, self).dispatch(*args, **kwargs)


    def get_form_kwargs(self, **kwargs):
        kwargs = super(IniciarProyecto, self).get_form_kwargs(**kwargs)
        kwargs['initial']['estado'] = 'INI'
        return kwargs

    def get_success_url(self, **kwargs):
        kwargs = super(IniciarProyecto, self).get_form_kwargs(**kwargs)
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk'])
        return reverse('configurar',args=[proyecto.pk])

from reportlab.pdfgen import canvas
from django.http import HttpResponse

def reporte_pdf(request, pk):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte del proyecto.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    p.drawString(210, 800, "1 - Cantidad de Trabajos en curso por equipo.")
    proyecto = Proyecto.objects.get(pk=pk)
    j=750
    p.setFont('Helvetica', 8)
    p.drawString(100, j, proyecto.nombre + ': ' + 'Estado  ' + proyecto.estado)
    equipo = Miembro.objects.filter(proyecto=proyecto.pk)
    sprints = Sprint.objects.filter(proyecto = proyecto.pk).filter(estado=2)
    j = j-20
    for sp in sprints:
          user_story = us.objects.filter(sprint = sp.pk)
          p.drawString(120, j, sp.nombre)
          j = j-20
          for eq in equipo:
              p.drawString(140, j, '* ' + eq.usuario.username)
              j=j-20
              for hu in user_story:
                  if hu.responsable.usuario.username == eq.usuario.username:
                        p.drawString(160, j, '- ' + hu.nombre)
                        j=j-20

    p.showPage()
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    miembros = Miembro.objects.filter(proyecto = proyecto.pk)
    p.drawString(200, 800, "2 - Cantidad de Trabajos por usuario, pendiente, en curso y finalizado.")
    j=750

    for usuario_system in miembros :
                p.setFont('Helvetica', 8)
                p.drawString(100, j, usuario_system.usuario.username)
                user_story = us.objects.filter(responsable = usuario_system)
                j = j-20
                for hu in user_story:
                            p.drawString(120, j, '- ' + hu.nombre)
                            j=j-20

    p.showPage()


    p.drawString(210, 800, "3 - Lista de Actividades para completar un proyecto.")
    j=750


    fluj = Flujos.objects.filter(proyecto = proyecto.pk)
    j = j-20
    for f in fluj:
         p.setFont('Helvetica', 8)
         p.drawString(120, j, f.nombre)
         acti = Actividad.objects.filter(flujo = f.pk).order_by('orden')
         j = j-20
         for a in acti:
               p.drawString(140, j, str(a.orden) + ': ' + a.nombre)
               j = j-20

    p.showPage()


    p.drawString(210, 800, "5 - Product BackLog por proyectos .")
    j=750

    p.setFont('Helvetica', 8)
    p.drawString(100, j, proyecto.nombre)
    user_story = us.objects.filter(proyecto = proyecto.pk).order_by('prioridad')
    j = j-20

    p.drawString(120, j, 'Nombre del Us')
    p.drawString(200, j, '      Prioridad')
    j = j-20
    for u in user_story:
            p.drawString(120, j, u.nombre + '          ' + str(u.prioridad))
            j = j-20


    p.showPage()

    proyectos = Proyecto.objects.all()
    p.drawString(210, 800, "5 - Sprint BackLog por proyectos .")
    j=750


    p.setFont('Helvetica', 8)
    p.drawString(100, j, proyecto.nombre)
    sprints = Sprint.objects.filter(proyecto = proyecto.pk)
    j = j-20
    for s in sprints:
          p.drawString(120, j, s.nombre)
          user_story = us.objects.filter(sprint = s.pk)
          j = j-20
          for hu in user_story:
                  p.drawString(140, j, hu.nombre + ' RESPONSABLE:  ' + hu.responsable.usuario.username)
                  j = j-20

    p.showPage()

    p.drawString(210, 800, "6 - Tiempo estimado y tiempo en curso.")
    j=750
    j = j-20
    sprint = Sprint.objects.filter(proyecto=proyecto.pk)
    for s in sprint:
        sprint_dias = s.duracion_dias
        miembros = Miembro.objects.filter(proyecto=proyecto.pk)

        horas_estimadas=0

        for miembro in miembros:
            horas_estimadas+=miembro.horas_por_dia

        xdata =[i + 1 for i in range(sprint_dias)]

        ydataestimado= [horas_estimadas*(sprint_dias-i) for i in range(sprint_dias)]


        datose = []
        dias = []

        for ye in ydataestimado:
            datose.append(ye)

        if s.estado.pk == 2:
            ydata2real = generar_horas_trabajadas(s.pk, ydataestimado,horas_estimadas*s.duracion_dias)
            datosr = []
            for yr in ydata2real:
                datosr.append(yr)

            data = [datose,datosr]
        else:
            data = [datose]

        drawing = Drawing(400, 200)


        for d in xdata:
            dias.append(str(d))


        lc = HorizontalLineChart()
        lc.x = 50
        lc.y = 50
        lc.height = 200
        lc.width = 400
        lc.data = data
        lc.joinedLines = 1
        lc.categoryAxis.categoryNames = dias
        lc.categoryAxis.labels.boxAnchor = 'n'
        lc.valueAxis.valueMin = 0
        lc.valueAxis.valueMax = horas_estimadas*sprint_dias
        lc.valueAxis.valueStep = 10
        lc.lines[0].strokeWidth = 1.5
        lc.lines[1].strokeWidth = 1.5
        drawing.add(lc)

        renderPDF.draw(drawing, p, 50, 500)

        p.showPage()


    p.showPage()
    p.save()
    return response



def generar_horas_trabajadas(pk,ydata,horas_estimadas):
    sprint = Sprint.objects.get(pk=pk)
    user_stories = us.objects.filter(sprint=pk)
    registros=[]
    for user_story in user_stories:
        registros += registroTrabajoUs.objects.filter(us=user_story)

    registros=sorted(registros,key=registroTrabajoUs.getKey)

    fecha_inicial = registros[0].fecha_hora_creacion

    horas_reales = range(sprint.duracion_dias)

    horas_disponibles = horas_estimadas

    for i in range(sprint.duracion_dias):
        registros=[]

        for user_story in user_stories:
            registros+=registroTrabajoUs.objects.filter(us=user_story).filter(fecha_hora_creacion=fecha_inicial)

        horas=0

        for registro in registros:
            horas=horas+ registro.horas_dedicadas

        horas_reales[i]=horas_disponibles

        horas_disponibles-=horas

        fecha_inicial=fecha_inicial+ datetime.timedelta(days=1)

    return [horas_reales[i] for i in range(sprint.duracion_dias)]