from django import forms
from django.forms import DateField, ModelForm, HiddenInput
from django.contrib.admin.widgets import AdminDateWidget
from flujos.models import Flujos, Actividad


class FlujosForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlujosForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        fecha_creacion = DateField(widget=AdminDateWidget)
        fecha_fin = DateField(widget=AdminDateWidget)
        self.fields['proyecto'].widget = HiddenInput()

    class Meta:
        model = Flujos
        fields = ('nombre','proyecto' , 'descripcion')



class FlujosUpdateForm(ModelForm):

    """def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    class Meta:
        model = Flujos
        fields = ('nombre', 'descripcion')


class ActividadForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ActividadForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['flujo'].widget = HiddenInput()

    class Meta:
        model = Actividad
        fields = ('nombre', 'orden', 'flujo')




class ActividadesUpdateForm(ModelForm):

    """def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    class Meta:
        model = Actividad
        fields = ('nombre', 'orden')
