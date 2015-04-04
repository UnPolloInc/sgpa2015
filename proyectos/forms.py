from django.forms import DateField

__author__ = 'alforro'

from django import forms
from django.contrib.admin.widgets import AdminDateWidget




from proyectos.models import Proyecto

class ProyectoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        fecha_inicio = DateField(widget=AdminDateWidget)
        fecha_fin = DateField(widget=AdminDateWidget)

    class Meta:
        model = Proyecto
        fields = ('nombre','lider_proyecto', 'fecha_inicio','fecha_fin', 'estado', 'descripcion','observaciones')

    def clean_fecha_inicio_menor_fecha_fin(self):
        diccionario_limpio = self.cleaned_data
        fecha_inicio = diccionario_limpio.get('fecha_inicio')
        fecha_fin = diccionario_limpio.get('fecha_fin')

        if fecha_inicio > fecha_fin:
            raise forms.ValidationError("La fecha de inicio es mayor a la de fin")

        return fecha_inicio
