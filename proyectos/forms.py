__author__ = 'alforro'

from django import forms
from django.forms import DateField, ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from proyectos.models import Proyecto

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

