from django.contrib import admin
from .models import producto, movimiento, stock

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["name","descripcion"]
    list_editable = ["descripcion"]
    list_filter = ["name"]


class MovimientoAdmin(admin.ModelAdmin):
    list_display = ["fecha_ingreso","ingreso","fecha_egreso","egreso","ubicacion_actual"]
    list_editable = ["ingreso","egreso","ubicacion_actual"]    

admin.site.register(producto, ProductoAdmin)
admin.site.register(movimiento,MovimientoAdmin)
admin.site.register(stock)
