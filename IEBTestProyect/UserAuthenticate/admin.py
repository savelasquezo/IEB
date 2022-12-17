from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Proyect, Wireline, SavesProyects

class ProyectAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nmproy",
        "typroy"
        )

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
    
class SavesProyectsAdmin(admin.ModelAdmin):
    
    
    list_display = (
        "savename",
        "username",
        "nmproy",
        "current",
        "voltage",
        "ampacity",
        "new_current",
        "datenow"
        )

admin.site.register(Usuario, UserAdmin)
admin.site.register(Proyect, ProyectAdmin)
admin.site.register(Wireline, WirelineAdmin)
admin.site.register(SavesProyects, SavesProyectsAdmin)






