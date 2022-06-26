from django.db import models


class Parroquia(models.Model):
	opcionesTipo = (
	('urbana', 'Urbana'),
	('rural', 'Rural'),
	)

	nombre = models.CharField('Nombre', max_length=50)
	tipo = models.CharField(max_length=25, choices=opcionesTipo)

	def __str__(self):
		return "%s - %s" % (self.nombre,
			self.tipo
			)

class Barrio(models.Model):
	parques = (
	(1, '1'),
	(2, '2'),
	(3, '3'),
	(4, '4'),
	(5, '5'),
	(6, '6')
	)

	nombreB = models.CharField('Nombre', max_length=50)
	nroViviendas = models.IntegerField('Numero viviendas')
	nroParques = models.IntegerField('Numero parques', choices=parques)
	nroEdificios = models.IntegerField('Numero edificios')

	parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE,
		related_name='barrios')

	def __str__(self):
		return "Nombre: %s - Numero viviendas: %d - Numero parques: %d - Numero edificios: %d" % (self.nombreB,
			self.nroViviendas,
			self.nroParques,
			self.nroEdificios
			)
