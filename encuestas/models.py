from django.db import models

# Create your models here.
class Pregunta(models.Model):    
    pregunta_text = models.CharField(max_length=200, )
    fecha_pub = models.DateTimeField("date published")

    def __str__(self):
        return self.pregunta_text

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=200)
    votaciones = models.IntegerField(default=0)

    def __str__(self):
        return self.opcion_text
    
