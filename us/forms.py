from django import forms
from django.forms import DateField, ModelForm, HiddenInput
from django.contrib.admin.widgets import AdminDateWidget
from flujos.models import Actividad
from us.models import us, registroTrabajoUs
from Notificaciones.views import notificar_asignacion_us, notificar_creacion_us, notificar_mod_us, notificar_generico


class AprobarForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AprobarForm, self).__init__(*args, **kwargs)
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
        self.fields['fecha_hora_creacion'].widget = HiddenInput()
    class Meta:
        model = registroTrabajoUs
        fields = ('descripcion','horas_dedicadas','us','archivo_adjunto','fecha_hora_creacion')




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
                us.estado = 'DONE'
            elif us.estado == 'DONE':
                try:
                    actividad = Actividad.objects.filter(orden = us.actividad.orden+1)
                    us.actividad=actividad.get(flujo=us.flujo)
                    us.estado='TODO'
                except:
                    #falta que el lider pueda finalizar el user storie aca.
                    us.save()
            us.save()
        return us