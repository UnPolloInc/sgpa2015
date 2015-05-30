from django import forms
from django.contrib.auth.models import Permission
from django.forms import ModelForm, HiddenInput
from roles.models import Rol

__author__ = 'alforro'


class RolForm(ModelForm):
    """
    Clase para crear Proyecto
    """
    permissions = forms.ModelMultipleChoiceField(Permission.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__( self, pass_a_Q_object=None, *args, **kwargs ):

        super(RolForm, self).__init__(*args, **kwargs)
        self.fields['proyecto'].widget = HiddenInput()
        permissions=['Can add us','Can add miembro','Can add rol','Can change rol','Can add sprint', 'Can add flujo','Can change flujo', 'Can add actividad',
                     'Can change actividad', 'Can add registro trabajo us',]
        self.fields['permissions'].queryset = Permission.objects.filter(name__in=permissions)
        """if pass_a_Q_object:
            self.fields['permissions'].queryset = Permission.objects.filter(pass_a_Q_object)
        """

    class Meta:
        model = Rol
        fields =('name','permissions','proyecto',)




class RolUpdateForm(ModelForm):

    """
    Clase para modificar Roles.
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    """
    permissions = forms.ModelMultipleChoiceField(Permission.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__( self, pass_a_Q_object=None, *args, **kwargs ):

        super(RolUpdateForm, self).__init__(*args, **kwargs)

        permissions=['Can add us','Can add miembro','Can add rol','Can change rol','Can add sprint', 'Can add flujo','Can change flujo', 'Can add actividad',
                     'Can change actividad', 'Can add registro trabajo us',]
        self.fields['permissions'].queryset = Permission.objects.filter(name__in=permissions)

    class Meta:
        model = Rol
        fields = ('name', 'permissions', )

