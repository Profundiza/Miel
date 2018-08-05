from django import forms

from .models import *


class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ('nombre', 'marca', 'medida', 'cantidad', 'costo')


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre', 'medida', 'cantidad')


class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = ('nombre', 'precio')
