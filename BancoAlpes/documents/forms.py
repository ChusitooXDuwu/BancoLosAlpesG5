from django import forms
from .models import Documento


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'Cliente',
            'Tipo',
            'Estado',
            'Archivo',
            'Score confiabilidad',
        ]

        labels = {
            'Cliente' : 'Cliente',
            'Tipo' : 'Tipo',
            'Estado' : 'Estado',
            'Archivo' : 'Archivo',
            'Score confiabilidad' : 'Score confiabilidad',
        }