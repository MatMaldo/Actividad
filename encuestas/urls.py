from django.urls import path

from . import views

urlpatterns = [
    # ex: /encuestas/
    path("", views.index, name="index"),

    # ex: /encuestas/pregunta/5/
    path("pregunta/<int:pregunta_id>/", views.get_pregunta, name="get_pregunta"),

    # /encuestas/pregunta/eliminar/5/
    path("pregunta/eliminar/<int:pregunta_id>/", views.delete_pregunta, name="delete_pregunta"),

    # /encuestas/pregunta/agregar
    path("pregunta/agregar/", views.add_pregunta, name="add_pregunta"),
]