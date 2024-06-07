from django import forms
from .models import Pregunta
from django.forms import ModelForm

#para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PreguntaForm(ModelForm):
    class Meta:
        model = Pregunta
        fields = "__all__"
        # fields = ["pregunta_text", "fecha_pub"]
        widgets = { 'fecha_pub' : forms.DateTimeInput( attrs = {'type':'datetime-local'} )}

class FormaRegistro(UserCreationForm):
    #Hace al campo de email sea obligatorio
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')