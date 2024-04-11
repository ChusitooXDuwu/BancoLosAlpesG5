from django import forms
from .models import Documento


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'cliente',
            'tipo',
            'estado',
            'archivo',
            'score confiabilidad',
        ]

        labels = {
            'cliente' : 'Cliente',
            'tipo' : 'Tipo',
            'estado' : 'Estado',
            'archivo' : 'Archivo',
            'score confiabilidad' : 'Score Confiabilidad',
        }