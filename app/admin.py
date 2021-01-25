from django.contrib import admin
from .models import producto, conacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["name","descripcion"]
    list_editable = ["descripcion"]
    list_filter = ["name"]




admin.site.register(producto, ProductoAdmin)
admin.site.register(conacto)
