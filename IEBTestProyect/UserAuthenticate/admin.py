from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Proyect, Wireline, SavesProyects


class ProyectAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nmproy",
        "typroy"
        )

    list_filter = ['nmproy','typroy']
    search_fields = ['user']

class WirelineAdmin(admin.ModelAdmin):
    list_display = (
        "cod_wireline",
        "material",
        "ampacity",
        "new_voltage",
        "new_thickness",
        "new_diameter",
        "new_current"
        )

    list_filter = ['material','ampacity']
    search_fields = ['cod_wireline']

class SavesProyectsAdmin(admin.ModelAdmin):
    
    
    list_display = (
        "savename",
        "username",
        "nmproy",
        "current",
        "voltage",
        "ampacity",
        "new_current"
        )

    list_filter = ['nmproy','datenow']
    search_fields = ['savename']

admin.site.register(Usuario, UserAdmin)
admin.site.register(Proyect, ProyectAdmin)
admin.site.register(Wireline, WirelineAdmin)
admin.site.register(SavesProyects, SavesProyectsAdmin)






