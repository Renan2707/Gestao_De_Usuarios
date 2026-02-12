from core.models.usuario import Usuario
from django import forms

class AddUsuarioForm(forms.ModelForm):
    STATUS_CHOICES = [
        (True, 'Ativo'),
        (False, 'Inativo'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select)

    class Meta:
        model = Usuario
        fields = ['nome', 'cargo', 'status']