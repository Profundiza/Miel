from django.contrib import admin

from .models import *

admin.site.register(CustomUser)
admin.site.register(Proveedor)
admin.site.register(Ingrediente)
admin.site.register(Receta)
admin.site.register(RecetaComp)
admin.site.register(Platillo)
admin.site.register(Restaurante)
