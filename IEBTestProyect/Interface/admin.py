from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import UserIEB, Proyect, Wireline, SavesProyects

admin.site.unregister(Group)

class IEBAdminSite(admin.AdminSite):
    index_title = 'Panel Administrativo'
    verbose_name = "IEB"

admin_site = IEBAdminSite()
admin.site = admin_site

admin_site.site_header = "IEB-Ingenieria Especializada"

class UserBaseAdmin(UserAdmin):
    
    fieldsets = (
        ("Autenticacion", {"fields": ("username", "password","is_active")}),
        ("Informacion", {"fields": ("first_name", "last_name","email","date_joined")}),
        )

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

admin.site.register(UserIEB, UserBaseAdmin)
admin.site.register(Proyect, ProyectAdmin)
admin.site.register(Wireline, WirelineAdmin)
admin.site.register(SavesProyects, SavesProyectsAdmin)





