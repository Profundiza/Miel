from django import forms

from .models import *


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseModelForm, self).__init__(*args, **kwargs)


class ProveedorForm(BaseModelForm):
    class Meta:
        model = Proveedor
        fields = ('nombre', 'telefono', 'representante', 'telefono_de_representante', 'correo_electronico')

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.fields['telefono'].error_messages = {'invalid_phone_number': 'Phone number must be entered in the format: \'+999999999\'. Up to 15 digits allowed.'}


class IngredienteForm(BaseModelForm):
    class Meta:
        model = Ingrediente
        fields = ('nombre', 'marca', 'medida', 'cantidad', 'costo',  'proveedor')


class RecetaForm(BaseModelForm):
    class Meta:
        model = Receta
        fields = ('nombre', 'medida', 'cantidad')


class RecetaCompForm(BaseModelForm):
    class Meta:
        model = RecetaComp
        fields = ('medida', 'cantidad')


class PlatilloForm(BaseModelForm):
    class Meta:
        model = Platillo
        fields = ('nombre', 'precio', 'bebida')


class PlatilloIngForm(BaseModelForm):
    class Meta:
        model = PlatilloIng
        fields = ('cantidad', 'medida')


class PlatilloRecForm(BaseModelForm):
    class Meta:
        model = PlatilloRec
        fields = ('cantidad', 'medida')
