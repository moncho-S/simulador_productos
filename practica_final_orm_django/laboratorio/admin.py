from django.contrib import admin
from .models import *
# Register your models here.
class LaboratorioAdmin(admin.ModelAdmin):
    list_display =['id','nombre']
    ordering=['id']
class ProductoAdmin(admin.ModelAdmin):
    list_display =['id','nombre','laboratorio','f_fabricacion','p_costo','p_venta']
    ordering=('nombre','laboratorio')
    list_filter =['nombre','laboratorio']
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display =['id','nombre','laboratorio']


admin.site.register(DirectorGeneral,DirectorGeneralAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Laboratorio,LaboratorioAdmin)