from django.db import models

# Create your models here.
class Tarea(models.Model):
	codigo = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	estado = models.BooleanField(default=False)
	creacion = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-creacion",]
                                                                                                                                                                                                                                                                                        
	def __str__(self):
		return self.codigo

