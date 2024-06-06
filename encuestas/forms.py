from django import forms
from .models import Pregunta
from django.forms import ModelForm

class PreguntaForm(ModelForm):
    class Meta:
        model = Pregunta
        fields = "__all__"
        # fields = ["pregunta_text", "fecha_pub"]
        widgets = { 'fecha_pub' : forms.DateTimeInput( attrs = {'type':'datetime-local'} )}