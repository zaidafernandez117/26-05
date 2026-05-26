from django.db import models

# Create your models here.
class alumnos(Models.Model):
    id_alumnos=autoField(primary_key=true)
    dni=models.TextField(max_length=10)
    apellido=models.TextField(max_length=35)
    nombre=models.TextField(max_length=35)
    edad=models.IntegerField()
    calle=models.TextField(max_length=50)
    altuta=models.IntegerField()

    def __str__(self):
        return self.dni