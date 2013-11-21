from django.db import models

# Create your models here.

class Material(models.Model):
	UNIDADES_DE_COMPRA = (
	    ('metro', 'Metro'),
	    ('Kilo', 'Kilo'),
	    ('paquete', 'Paquete'),
	    ('unidades', 'Unidades'),
    )
	nombre=models.CharField(max_length=50,unique=True)
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)
	precio_por_unidad = models.DecimalField(max_digits=9,decimal_places=2)
	unidad_de_compra= models.CharField(max_length=12, choices=UNIDADES_DE_COMPRA)

	def __unicode__(self):
		return '%s' % self.nombre

	def precio_a_compra(self):
		return 'S/.%s por %s' %(self.precio_por_unidad,self.unidad_de_compra)

	class Meta:
		verbose_name_plural = "Materiales"


class Compra(models.Model):
	material= models.ForeignKey('Material')
	fecha = models.DateTimeField(auto_now=True)
	cantidad = models.IntegerField(default=0)
	soles_comprados = models.DecimalField(max_digits=9,decimal_places=2)
	unidad_compra= models.CharField(max_length=10)

	def __unicode__(self):
		return '%s' %self.material

class Stock(models.Model):
	material =  models.ForeignKey('Material')
	cantidad = models.IntegerField(default=0)
	actualizado = models.DateTimeField(auto_now=True)
	total_cant = models.IntegerField(default=0)
	unidad_compra= models.CharField(max_length=10)
	total_soles = models.DecimalField(max_digits=9,decimal_places=2,default=0)

	def __unicode__(self):
		return '%s' % self.material

	def canti(self):
		return '%s de %s' %(self.cantidad,self.unidad_compra)

class Firme(models.Model):
	COLOR = (
	    ('fucsia', 'fucsia'),
	    ('negro', 'negro'),
	    ('azul', 'azul'),
	    ('lila', 'lila'),
	    ('beig', 'beig'),
	    ('celeste', 'celeste'),
    )
	color=models.CharField(max_length=50,choices=COLOR)
	talla=models.CharField(max_length=5)
	precio_par=models.DecimalField(max_digits=9,decimal_places=2)

	def __unicode__(self):
		return "%s-%s" %(self.color,self.talla)

class PedidoFirme(models.Model):
	firme=models.ForeignKey("Firme")
	cantidad=models.IntegerField(default=0)
	fecha=models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s" %self.firme

class StockFirme(models.Model):
	firme=models.ForeignKey("Firme")
	cantidad_compra=models.IntegerField(default=0)
	cantidad_usado=models.IntegerField(default=0)
	fecha=models.DateTimeField(auto_now=True)
	total_cant=models.IntegerField(default=0)
