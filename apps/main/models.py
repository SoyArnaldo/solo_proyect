from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class ConocimientoManager(models.Manager):
	def first_conocimiento(self):
	# Subconsulta para obtener el ID del primer conocimiento de cada usuario
		subquery = self.filter(
			author=models.OuterRef('author')
		).order_by('public').values('pk')[:1]

	# Consulta principal para obtener el primer conocimiento de cada usuario
		obj = self.filter(
			pk=models.Subquery(subquery)
		)
		return obj

class Conocimiento(models.Model):
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='conocimientos')
	conocimiento = models.TextField()
	public = models.DateTimeField("Publicado", auto_now_add=True)
	modified = models.DateTimeField("Modificado", auto_now=True)
	link_video = models.URLField()

	class Meta:
		verbose_name_plural = "Conocimientos"
		db_table = "conocimiento"
		ordering = ["-public"]
	
	objects = ConocimientoManager()
	def __str__(self) -> str:
		return f"{self.author} + {self.email}"
