from django.contrib.auth.models import User, Group, AbstractUser
from django.db import models


class Restaurante(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# TODO Move to accounts app
class CustomUser(AbstractUser):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)


class Proveedor(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    representante = models.CharField(max_length=50)
    telefono_de_representante = models.IntegerField()
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT, null=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    costo = models.FloatField()
    medida = models.CharField(max_length=30, choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'unit'), ('dozen', 'dozen')])
    cantidad = models.FloatField()
    unit_cost = models.FloatField(null=True, blank=True)

    def get_unit_cost(self):
        try:
            uc = float(self.costo) / float(self.cantidad)
        except (ZeroDivisionError, TypeError):
            uc = 0
        return uc

    def save(self, *args, **kwargs):
        self.unit_cost = self.get_unit_cost()
        super(Ingrediente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    ingredientes = models.ManyToManyField(Ingrediente, through='RecetaComp')
    medida = models.CharField(max_length=30, choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL','mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'unit'), ('dozen', 'dozen')])
    cantidad = models.FloatField()
    costo = models.FloatField(null=True)
    unit_cost = models.FloatField(null=True)

    def get_unit_cost(self):
        try:
            uc = int(self.costo) / int(self.cantidad)
        except (ZeroDivisionError, TypeError):
            uc = 0
        return uc

    def save(self, *args, **kwargs):
        self.unit_cost = self.get_unit_cost()
        super(Receta, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class RecetaComp(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    cantidad = models.FloatField()


class Platillo(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    costo = models.FloatField(null=True)
    precio = models.FloatField()
    costo_percentaje = models.FloatField(null=True, blank=True)
    ganancia = models.FloatField(null=True, blank=True)
    ingredientes = models.ManyToManyField(Ingrediente, through='PlatilloIng')
    recetas = models.ManyToManyField(Receta, through='PlatilloRec')
    bebida = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.ganancia = self.precio - self.costo
        self.costo_percentaje = 100 * self.costo / self.precio
        super(Platillo, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class PlatilloIng(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    cantidad = models.FloatField()

    def __str__(self):
        return self.platillo.nombre + " " + self.ingrediente.name


class PlatilloRec(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.PROTECT)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    cantidad = models.FloatField()
