__author__ = 'chelox'


from django import forms
from django.forms import DateField, ModelForm, HiddenInput
from django.contrib.admin.widgets import AdminDateWidget
from mensajes.models import mensajes

class mensajesForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(mensajesForm, self).__init__(*args, **kwargs)
        self.fields['proyecto'].widget = HiddenInput()
        self.fields['remitente'].widget = HiddenInput()

    class Meta:
        model = mensajes
        fields = ('proyecto','remitente','destinatario','texto_mensaje')



class mensajesUpdateForm(ModelForm):

    """def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    class Meta:
        model = mensajes
        fields = ('remitente','destinatario','texto_mensaje')



#class PriorizarForm(ModelForm):

#    """def __init__(self, *args, **kwargs):
#        super(ModelForm, self).__init__(*args,
#**kwargs)
#        self.fields['first_name'].required = True
#        self.fields['last_name'].required = True
#    """
#    class Meta:
#        model = us
#        fields = ('prioridad',)

