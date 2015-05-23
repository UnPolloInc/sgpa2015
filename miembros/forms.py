from roles.models import Rol

__author__ = 'jorgeflor'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import ModelForm, HiddenInput
from miembros.models import Miembro
from Notificaciones.views import notificar_asignacion_proyecto

class MiembroForm(ModelForm):

    def __init__(self, *args, **kwargs):
        proyecto = kwargs.pop('proyecto')
        super(MiembroForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].required = True
        self.fields['rol'].queryset = Rol.objects.filter(proyecto=proyecto)
        self.fields['proyecto'].widget = HiddenInput()
        self.fields['usuario'].widget = HiddenInput()

    def save(self, commit=True):
        # Save the provided password in hashed format
        miembro = super(MiembroForm, self).save(commit=False)
        #user.set_password(self.cleaned_data["password1"])
        if commit:
            miembro.save()
            grupo = Group.objects.get(name=miembro.rol.name)
            grupo.user_set.add(miembro.usuario)
            notificar_asignacion_proyecto(miembro.usuario,miembro.proyecto)
        return miembro



    class Meta:
        model = Miembro
        fields = ('proyecto','usuario', 'horas_por_dia','rol')

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
        fields = ('horas_por_dia',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        miembro = super(MiembroForm, self).save(commit=False)
        #user.set_password(self.cleaned_data["password1"])
        if commit:
            miembro.save()
            miembro.usuario.groups.clear()
            grupo = Group.objects.get(name=miembro.rol.name)
            grupo.user_set.add(miembro.usuario)
            notificar_asignacion_proyecto(miembro.usuario,miembro.proyecto)
        return miembro

