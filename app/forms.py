from django import forms
from .models import conacto


class contactoForm(forms.ModelForm):

    class Meta:
        model = conacto
        fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]
