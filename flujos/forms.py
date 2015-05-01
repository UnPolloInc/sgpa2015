from django import forms
from django.forms import DateField, ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from flujos.models import Flujos

class FlujosForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlujosForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        fecha_creacion = DateField(widget=AdminDateWidget)
        fecha_fin = DateField(widget=AdminDateWidget)

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

