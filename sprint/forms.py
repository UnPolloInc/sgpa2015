__author__ = 'chelox'


from django import forms
from django.forms import DateField, ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from sprint.models import Sprint

class SprintForm(ModelForm):
    """
    Clase para crear Sprint's
    """
    def __init__(self, *args, **kwargs):

        super(SprintForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        #fecha_inicio = DateField(widget=AdminDateWidget)
        #fecha_fin = DateField(widget=AdminDateWidget)


    class Meta:
        model = Sprint
        fields = ('nombre','proyecto', 'descripcion', 'duracion_dias', 'observaciones')

    def clean_duracion_dias_menor_quince(self):
        """
        Validacion de fecha, inicio menor a fin
        """
        diccionario_limpio = self.cleaned_data
        duracion_dias = diccionario_limpio.get('duracion_dias')

        if duracion_dias > 15:
            raise forms.ValidationError("La duracion del sprint no puede ser mayor a 15")

        return duracion_dias


class SprintUpdateForm(ModelForm):

    """
    Clase para modifica Proyectos.
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    class Meta:
        model = Sprint
        fields = ('nombre', 'proyecto','descripcion','duracion_dias','observaciones')

