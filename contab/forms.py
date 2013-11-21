from django import forms
from models import *

class MaterialAddForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('nombre', 'precio_por_unidad', 'unidad_de_compra',)

class ComprasForm(forms.ModelForm):
	class Meta:
		model = Compra
		exclude=("soles_comprados","unidad_compra")