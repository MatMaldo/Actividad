from django.http import HttpResponse
from django.shortcuts import redirect, render
from encuestas.forms import PreguntaForm, FormaRegistro
from encuestas.models import Pregunta


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
"""
def index(request):
    return HttpResponse("Estamos en el index")
"""
# localhost:8000/encuestas
def index(request):
    listado = Pregunta.objects.all()
    contexto = {"personas":listado}
    return render(request,'encuestas/index.html',contexto)

# localhost:8000/encuestas/pregunta/2
def get_pregunta(request, pregunta_id):
    resultado = Pregunta.objects.get(id=pregunta_id)
    contexto = {"pregunta":resultado}
    return render(request,'encuestas/preguntas_por_id.html',contexto)

# localhost:8000/encuestas/pregunta/eliminar/2
def delete_pregunta(request, pregunta_id):
    pregunta = Pregunta.objects.get(id=pregunta_id)
    pregunta.delete()
    return redirect('/encuestas/')

# localhost:8000/encuestas/pregunta/agregar
def add_pregunta(request):
    if request.method == 'GET':
        formulario = PreguntaForm()
        contexto = { 'formulario': formulario }
        return render(request,'encuestas/agregar_pregunta.html',contexto)        
    
    elif request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()      
            listado = Pregunta.objects.all()
            contexto = {"personas":listado, 'mensaje':'Se ha registrado una pregunta'}      
            return render(request,'encuestas/index.html',contexto)
        else:
            return HttpResponse('Error: Revise los datos del formulario')
    else:
        return redirect('/encuestas/')
    
def sign_up(request):
    if request.method == 'GET':
        form = FormaRegistro()
        formulario = ({'form':form})
        return render(request,'encuestas/signup.html',formulario)
    
    elif request.method == 'POST':
        return redirect('/encuestas/')