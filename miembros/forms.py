__author__ = 'jorgeflor'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput
from miembros.models import Miembro


class MiembroForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MiembroForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].required = True
        self.fields['proyecto'].widget = HiddenInput()
        self.fields['usuario'].widget = HiddenInput()

    class Meta:
        model = Miembro
        fields = ('proyecto','usuario')

class MiembroUpdateForm(ModelForm):

    """
    Metodo para modificar clientes
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    class Meta:
        model = Miembro
        fields = ('proyecto','usuario')

