__author__ = 'alforro'

from django import forms
from django.forms import DateField, ModelForm, HiddenInput
from django.contrib.admin.widgets import AdminDateWidget
from proyectos.models import Proyecto
from Notificaciones.views import notificar_mod_proyecto, notificar_creacion_proyecto

class ProyectoForm(ModelForm):
    """
    Clase para crear Proyecto
    """
    def __init__(self, *args, **kwargs):

        super(ProyectoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        fecha_inicio = DateField(widget=AdminDateWidget)
        fecha_fin = DateField(widget=AdminDateWidget)

    class Meta:
        model = Proyecto
        fields = ('nombre','lider_proyecto', 'cliente', 'fecha_inicio', 'fecha_fin', 'descripcion', 'observaciones')

    def clean_fecha_inicio_menor_fecha_fin(self):
        """
        Validacion de fecha, inicio menor a fin
        """
        diccionario_limpio = self.cleaned_data
        fecha_inicio = diccionario_limpio.get('fecha_inicio')
        fecha_fin = diccionario_limpio.get('fecha_fin')

        if fecha_inicio > fecha_fin:
            raise forms.ValidationError("La fecha de inicio es mayor a la de fin")

        return fecha_inicio

    def save(self, commit=True):
        # Save the provided password in hashed format
        proyecto = super(ProyectoForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            proyecto.save()
            notificar_creacion_proyecto(proyecto.lider_proyecto,proyecto)
            notificar_creacion_proyecto(proyecto.cliente,proyecto)
        return proyecto


class ProyectoUpdateForm(ModelForm):

    """
    Clase para modifica Proyectos.
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    class Meta:
        model = Proyecto
        fields = ('nombre', 'lider_proyecto','descripcion', 'observaciones')

    def save(self, commit=True):
        # Save the provided password in hashed format
        proyecto = super(ProyectoUpdateForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            proyecto.save()
            notificar_mod_proyecto(proyecto.lider_proyecto,proyecto)
        return proyecto

class ProyectoIniciarForm(ModelForm):

    """
    Clase para iniciar proyectos.
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    def __init__(self, *args, **kwargs):
        super(ProyectoIniciarForm, self).__init__(*args, **kwargs)
        self.fields['estado'].widget = HiddenInput()

    class Meta:
        model = Proyecto
        fields = ('estado',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        proyecto = super(ProyectoIniciarForm, self).save(commit=False)
        #proyecto.set_password(self.cleaned_data["password1"])
        if commit:
            proyecto.save()
            notificar_mod_proyecto(proyecto.lider_proyecto,proyecto)
        return proyecto