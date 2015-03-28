from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import Usuario
__author__ = 'alforro'


class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = Usuario
        fields = ('username','email', 'first_name', 'last_name', 'cedula','telefono', 'direccion')
