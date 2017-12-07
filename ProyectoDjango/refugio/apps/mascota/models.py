from django.db import models

class Mascota(models.Model):
	folio = models.CharField(max_length = 10, primary_key= True)
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length = 10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
