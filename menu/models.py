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
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    sales_rep = models.CharField(max_length=50)
    sales_rep_phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Ingrediente(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, default='temp')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    cost = models.FloatField(default=0)
    measurement = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit_cost = models.FloatField(null=True)

    def get_unit_cost(self):
        try:
            uc = self.cost / self.quantity
        except (ZeroDivisionError, TypeError):
            uc = 0
        return uc

    def save(self, *args, **kwargs):
        self.unit_cost = self.get_unit_cost()
        super(Ingrediente, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Receta(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    ingredientes = models.ManyToManyField(Ingrediente, through='RecetaComp')
    measurement = models.CharField(max_length=30)
    quantity = models.FloatField()
    cost = models.FloatField(null=True)
    unit_cost = models.FloatField(null=True)

    def get_unit_cost(self):
        try:
            uc = self.cost / self.quantity
        except (ZeroDivisionError, TypeError):
            uc = 0
        return uc

    def save(self, *args, **kwargs):
        self.unit_cost = self.get_unit_cost()
        super(Receta, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class RecetaComp(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    quantity = models.FloatField()


class Platillo(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    costo = models.FloatField(null=True)
    precio = models.FloatField()
    ingredientes = models.ManyToManyField(Ingrediente, through='PlatilloIng')
    recetas = models.ManyToManyField(Receta, through='PlatilloRec')
    bebida = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class PlatilloIng(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    quantity = models.FloatField()

    def __str__(self):
        return self.platillo.nombre + " " + self.ingrediente.name


class PlatilloRec(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.PROTECT)
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    quantity = models.FloatField()
