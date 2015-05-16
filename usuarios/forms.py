from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from usuarios.models import Usuario
from Notificaciones.views import notificar_creacion_usuario, notificar_mod_usuario
__author__ = 'alforro'


class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            notificar_creacion_usuario(user)
        return user

    class Meta:
        model = Usuario
        fields = ('username','email', 'is_superuser','first_name', 'last_name', 'cedula','telefono', 'direccion')

class UserUpdateForm(ModelForm):

    """def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    class Meta:
        model = Usuario
        fields = ('email', 'is_superuser','first_name', 'last_name','telefono', 'direccion')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserUpdateForm, self).save(commit=False)
        #user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            notificar_mod_usuario(user)
        return user