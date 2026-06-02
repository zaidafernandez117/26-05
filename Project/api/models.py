from django.db import models

# Create your models here.
class alumnos(models.Model):
    id_alumnos=models.AutoField(primary_key=True)
    dni=models.TextField(max_length=10)
    apellido=models.TextField(max_length=35)
    nombre=models.TextField(max_length=35)
    edad=models.IntegerField()
    calle=models.TextField(max_length=50)
    altuta=models.IntegerField()

    def __str__(self):
        return self.dni