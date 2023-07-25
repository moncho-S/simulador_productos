from django.db import models
import datetime
year_choices = []
for r in range(2015, (datetime.datetime.now().year+1)):
    year_choices.append((r,r))

# Create your models here.
class Laboratorio(models.Model):
    nombre=models.CharField( max_length=255)
    ciudad=models.CharField( max_length=255)
    pais=models.CharField( max_length=255)

    
    class Meta:
        verbose_name = ("laboratorio")
        verbose_name_plural = ("laboratorios")

    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre=models.CharField( max_length=255)
    laboratorio=models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad=models.CharField( max_length=255)
    

    class Meta:
        verbose_name = ("Director General")
        verbose_name_plural = ("Director Generals")

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField( max_length=255)
    laboratorio=models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion=models.IntegerField( choices=year_choices, default=datetime.datetime.now().year)
    p_costo=models.DecimalField( max_digits=10, decimal_places=2)
    p_venta=models.DecimalField( max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.nombre