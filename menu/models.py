from django.db import models


class Proveedor(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    sales_rep = models.CharField(max_length=50)
    sales_rep_phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Ingrediente(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, default='temp')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    cost = models.FloatField(default=0)
    measurement = models.CharField(max_length=30)
    quantity = models.FloatField()

    def __str__(self):
        return self.name


class Receta(models.Model):
    name = models.CharField(max_length=50)
    ingredientes = models.ManyToManyField(Ingrediente, through='RecetaComp')

    def __str__(self):
        return self.name


class RecetaComp(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    quantity = models.FloatField()


class Platillo(models.Model):
    costo = models.FloatField()
    precio = models.FloatField()
    ingredientes = models.ManyToManyField(Ingrediente, through='PlatilloIng')
    recetas = models.ManyToManyField(Receta, through='PlatilloRec')
    tipo = models.CharField(max_length=30)


class PlatilloIng(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.PROTECT)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    quantity = models.FloatField()


class PlatilloRec(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.PROTECT)
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    quantity = models.FloatField()
