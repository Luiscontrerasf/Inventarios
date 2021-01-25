from django import forms
from .models import conacto, producto

class contactoForm(forms.ModelForm):

    class Meta:
        model = conacto
        fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]


class productoForm(forms.ModelForm):

    class Meta:
        model = producto
        fields = '__all__'





