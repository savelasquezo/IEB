from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    """
    
    "IEBTestProyect/settings.py"
    AUTH_USER_MODEL = 'UserAuthenticate.Usuario'
    USERNAME_FIELD = 'username'
    """
    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

class Proyect(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name="Usuario")
    nmproy = models.CharField(max_length=64,verbose_name="Nm-Proyecto")
    typroy = models.CharField(max_length=64,verbose_name="Ty-Proyecto")

    class Meta:
        verbose_name = _("Asignacion")
        verbose_name_plural = _("Asignaciones")

class Wireline(models.Model):
    cod_wireline = models.BigAutoField(primary_key=True,verbose_name="Codigo")
    material = models.CharField(max_length=128,verbose_name="Material")
    ampacity = models.FloatField(verbose_name="Ampacidad")
    new_voltage = models.FloatField(verbose_name="Tension*")
    new_thickness = models.FloatField(verbose_name="Espesor*")
    new_diameter = models.FloatField(verbose_name="Diametro*")
    new_current = models.FloatField(verbose_name="Corriente*")

    class Meta:
        verbose_name = _("Cable")
        verbose_name_plural = _("Catalogo")
        

class SavesProyects(models.Model):
    
    savename = models.CharField(max_length=128,verbose_name="Seleccion",null=False)
    username = models.CharField(max_length=128,verbose_name="Usuario",null=False)
    nmproy = models.CharField(max_length=128,verbose_name="Nm-Proyecto",null=False)

    current = models.FloatField(verbose_name="Corriente",null=False)
    voltage = models.FloatField(verbose_name="Tension",null=False)
    ampacity = models.FloatField(verbose_name="Ampacidad",null=False)
    new_current = models.FloatField(verbose_name="Corriente*",null=False)
    message = models.CharField(verbose_name="Comentarios",max_length=256,blank=True,null=True)
    
    datenow = models.DateField(auto_now=False, auto_now_add=False,verbose_name="Fecha")

    class Meta:
        verbose_name = _("Seleccion")
        verbose_name_plural = _("Selecciones")
