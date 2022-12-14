from django.contrib import admin
from .models import Usuario, Proyect
from django.contrib.auth.admin import UserAdmin

class ProyectAdmin(admin.ModelAdmin):
    list_display = ("user","nmproy","typroy")

admin.site.register(Usuario, UserAdmin)
admin.site.register(Proyect, ProyectAdmin)


