from django import forms
from django.forms import DateField, ModelForm, HiddenInput
from django.contrib.admin.widgets import AdminDateWidget
from us.models import us


class usasigForm(ModelForm):

   class Meta:
        model = us
        fields = ('sprint', 'flujo', 'responsable')


class usForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(usForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['flujo'].widget = HiddenInput()
        self.fields['sprint'].widget = HiddenInput()
        self.fields['responsable'].widget = HiddenInput()
        self.fields['proyecto'].widget = HiddenInput()

    class Meta:
        model = us
        fields = ('nombre','valor_de_negocio', 'prioridad', 'valor_tecnico', 'historial', 'duracion_horas', 'proyecto', 'flujo', 'sprint', 'responsable')



class usUpdateForm(ModelForm):

   def __init__(self, *args, **kwargs):
        super(usUpdateForm, self).__init__(*args, **kwargs)
        self.fields['flujo'].widget = HiddenInput()
        self.fields['sprint'].widget = HiddenInput()
        self.fields['responsable'].widget = HiddenInput()
        self.fields['proyecto'].widget = HiddenInput()

   class Meta:
        model = us
        fields = ('nombre','valor_de_negocio', 'prioridad', 'valor_tecnico', 'historial', 'duracion_horas', 'sprint', 'flujo', 'responsable', 'proyecto')



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

