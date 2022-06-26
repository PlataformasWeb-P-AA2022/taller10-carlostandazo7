
from django.contrib import admin
from ordenamiento.models import *
# Register your models here.

class ParroquiaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo')
	search_fields = ('nombre', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
	list_display = ('nombreB', 'nroViviendas', 'nroParques', 'nroEdificios', 'parroquia')
	search_fields = ('nroParques', 'parroquia')

admin.site.register(Barrio, BarrioAdmin)
