from django.forms import ModelForm, HiddenInput
from django.utils.datetime_safe import date

from flujos.models import Actividad

from us.models import us, registroTrabajoUs

from Notificaciones.views import notificar_asignacion_us, notificar_creacion_us, notificar_mod_us
from db_file_storage.form_widgets import DBClearableFileInput

class AprobarForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AprobarForm, self).__init__(*args, **kwargs)
        self.fields['estado_de_aprobacion'].widget = HiddenInput()
        self.fields['proyecto'].widget = HiddenInput()
    class Meta:
        model = us
        fields = ('proyecto', 'estado_de_aprobacion',)

class CancelarForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CancelarForm, self).__init__(*args, **kwargs)
        self.fields['estado_de_aprobacion'].widget = HiddenInput()
        self.fields['proyecto'].widget = HiddenInput()
    class Meta:
        model = us
        fields = ('proyecto', 'estado_de_aprobacion',)


class usasigForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(usasigForm, self).__init__(*args, **kwargs)
        self.fields['sprint'].required = True
        self.fields['flujo'].required = True
        self.fields['responsable'].required = True
        self.fields['duracion_horas_en_sprint'].required = True

    class Meta:
        model = us
        fields = ('sprint', 'flujo', 'responsable', 'duracion_horas_en_sprint')

    def save(self, commit=True):
        # Save the provided password in hashed format
        us = super(usasigForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            actividades=Actividad.objects.filter(flujo=us.flujo).order_by('pk')
            us.actividad=actividades[0]
            us.save()
            notificar_asignacion_us(us.responsable.usuario,us.proyecto)
            #notificar_asignacion_us(us.proyecto.cliente,us.proyecto)
        return us


class usForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(usForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['flujo'].widget = HiddenInput()
        self.fields['sprint'].widget = HiddenInput()
        self.fields['responsable'].widget = HiddenInput()
        self.fields['proyecto'].widget = HiddenInput()
        self.fields['duracion_horas_en_sprint'].widget = HiddenInput()
        self.fields['actividad'].widget = HiddenInput()
        self.fields['estado'].widget = HiddenInput()
        self.fields['estado_de_aprobacion'].widget = HiddenInput()
    class Meta:
        model = us
        fields = ('nombre','valor_de_negocio', 'prioridad', 'valor_tecnico', 'descripcion', 'duracion_horas', 'proyecto', 'flujo', 'sprint', 'responsable', 'duracion_horas_en_sprint', 'actividad', 'estado', 'estado_de_aprobacion',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        us = super(usForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            us.save()
            notificar_creacion_us(us.proyecto.lider_proyecto,us.proyecto)
            #notificar_asignacion_us(us.proyecto.cliente,us.proyecto)
        return us

class usUpdateForm(ModelForm):

   class Meta:
        model = us
        fields = ('nombre','valor_de_negocio', 'prioridad', 'valor_tecnico', 'descripcion', 'duracion_horas', 'estado_de_aprobacion',)

   def save(self, commit=True):
        # Save the provided password in hashed format
        us = super(usUpdateForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            us.save()
            notificar_mod_us(us.proyecto.lider_proyecto,us.proyecto)
            #notificar_asignacion_us(us.proyecto.cliente,us.proyecto)
        return us


class PriorizarForm(ModelForm):

    """def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    class Meta:
        model = us
        fields = ('prioridad',)


class registroForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(registroForm, self).__init__(*args, **kwargs)
        self.fields['horas_dedicadas'].required = True
        self.fields['us'].widget = HiddenInput()
        self.fields['archivo_adjunto'].required = False

    class Meta:
        model = registroTrabajoUs
        fields = ('descripcion','horas_dedicadas','us','archivo_adjunto',)
        widgets = {
            'archivo_adjunto': DBClearableFileInput
        }



class CambiarEstadoUsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CambiarEstadoUsForm, self).__init__(*args, **kwargs)
        self.fields['estado'].widget = HiddenInput()

    class Meta:
        model = us
        fields = ('estado',)


    def save(self, commit=True):
        # Save the provided password in hashed format
        us = super(CambiarEstadoUsForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            if us.estado == 'TODO':
                us.estado = 'DOING'
            elif us.estado == 'DOING':
                try:
                    actividad = Actividad.objects.filter(orden = us.actividad.orden+1)
                    us.actividad=actividad.get(flujo=us.flujo)
                    us.estado='TODO'
                except:
                    #falta que el lider pueda finalizar el user storie aca.
#                    proyecto = Proyecto.objects.get(pk=us.proyecto.pk)
 #                   if self.request.user == proyecto.lider_proyecto:
                    us.estado='DONE'
                    us.save()
            elif us.estado == 'DONE':
                try:
                    actividad = Actividad.objects.filter(orden = us.actividad.orden+1)
                    us.actividad=actividad.get(flujo=us.flujo)
                    us.estado='TODO'
                except:
                    #falta que el lider pueda finalizar el user storie aca.
#                    proyecto = Proyecto.objects.get(pk=us.proyecto.pk)
 #                   if self.request.user == proyecto.lider_proyecto:
                    us.estado_de_aprobacion='FIN'
                    us.save()
            us.save()
        registro = registroTrabajoUs(us=us, descripcion="se finalizo el US", horas_dedicadas=0, fecha_hora_creacion = date.today(), archivo_adjunto=None )
        registro.save()
        return us

class AvanzarUsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AvanzarUsForm, self).__init__(*args, **kwargs)
        self.fields['estado'].widget = HiddenInput()

    class Meta:
        model = us
        fields = ('estado',)


    def save(self, commit=True):
        # Save the provided password in hashed format
        us = super(AvanzarUsForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            if us.estado == 'TODO':
                us.estado = 'DOING'
            elif us.estado == 'DOING':
                try:
                    actividad = Actividad.objects.filter(orden = us.actividad.orden+1)
                    us.actividad=actividad.get(flujo=us.flujo)
                    us.estado='TODO'
                except:
                    #falta que el lider pueda finalizar el user storie aca.
#                    proyecto = Proyecto.objects.get(pk=us.proyecto.pk)
 #                   if self.request.user == proyecto.lider_proyecto:
                    us.estado='DONE'
                    us.save()
            elif us.estado == 'DONE':
                try:
                    actividad = Actividad.objects.filter(orden = us.actividad.orden+1)
                    us.actividad=actividad.get(flujo=us.flujo)
                    us.estado='TODO'
                except:
                    #falta que el lider pueda finalizar el user storie aca.
#                    proyecto = Proyecto.objects.get(pk=us.proyecto.pk)
 #                   if self.request.user == proyecto.lider_proyecto:
                    us.estado_de_aprobacion='FIN'
                    us.save()
            us.save()
        registro = registroTrabajoUs(us=us, descripcion="se avanzo el estado", horas_dedicadas=0, fecha_hora_creacion = date.today(), archivo_adjunto=None )
        registro.save()
        return us




class RetrocederUsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RetrocederUsForm, self).__init__(*args, **kwargs)
        self.fields['estado'].widget = HiddenInput()

    class Meta:
        model = us
        fields = ('estado',)


    def save(self, commit=True):
        # Save the provided password in hashed format
        us = super(RetrocederUsForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:

            if us.estado == 'TODO':
                try:
                    actividad = Actividad.objects.filter(orden = us.actividad.orden-1)
                    us.actividad=actividad.get(flujo=us.flujo)
                    us.estado='DONE'
                except:
                    #falta que el lider pueda finalizar el user storie aca.
#                    proyecto = Proyecto.objects.get(pk=us.proyecto.pk)
 #                   if self.request.user == proyecto.lider_proyecto:
                    us.estado='TODO'
                    us.save()
            elif us.estado == 'DOING':
                us.estado = 'TODO'
            elif us.estado == 'DONE':
                us.estado= 'DOING'
            us.save()
        registro = registroTrabajoUs(us=us, descripcion="se retrocedio el estado", horas_dedicadas=0, fecha_hora_creacion = date.today(), archivo_adjunto=None )
        registro.save()
        return us


class CambiarActividadLiderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CambiarActividadLiderForm, self).__init__(*args, **kwargs)
        self.fields['flujo'].widget = HiddenInput()
        self.fields['estado'].widget = HiddenInput()
    class Meta:
        model = us
        fields = ('flujo', 'actividad','estado',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        us = super(CambiarActividadLiderForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            us.save()
            notificar_mod_us(us.proyecto.lider_proyecto,us.proyecto)
            #notificar_asignacion_us(us.proyecto.cliente,us.proyecto)
        return us

