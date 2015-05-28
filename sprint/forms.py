__author__ = 'chelox'


from django import forms
from django.forms import DateField, ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from sprint.models import Sprint
from django.forms.widgets import HiddenInput
from us.models import us





class FinalizarSprintForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(FinalizarSprintForm, self).__init__(*args, **kwargs)
        self.fields['estado'].widget = HiddenInput()

    class Meta:
        model = Sprint
        fields = ('estado',)


class EjecutarSprintForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EjecutarSprintForm, self).__init__(*args, **kwargs)
        self.fields['estado'].widget = HiddenInput()

    class Meta:
        model = Sprint
        fields = ('estado',)


class SprintForm(ModelForm):
    """
    Clase para crear Sprint's
    """
    def __init__(self, *args, **kwargs):
        super(SprintForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['proyecto'].widget = HiddenInput()


    class Meta:
        model = Sprint
        fields = ('nombre', 'proyecto', 'descripcion', 'duracion_dias', 'observaciones', 'estado')

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
        fields = ('nombre','descripcion','duracion_dias','observaciones')


class usUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(usUpdateForm, self).__init__(*args, **kwargs)
        self.fields['sprint'].required = True
        self.fields['flujo'].required = True
        self.fields['responsable'].required = True
        self.fields['duracion_horas_en_sprint'].required = True

    class Meta:
        model = us
        fields = ('sprint','flujo','responsable', 'duracion_horas_en_sprint')
