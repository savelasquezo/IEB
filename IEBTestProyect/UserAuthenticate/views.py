from datetime import datetime

from django.views.generic.base import TemplateView
from django.utils import timezone
from django.shortcuts import redirect, render

from .models import Proyect, SavesProyects
from .functions import Ampacity, QuerySelect

class HomeLogin(TemplateView):
    template_name='home.html'

class Workresults(HomeLogin):

    """Gets the values entered by the user and presents them in a form-like interface.
        Allowing the option to save the content in the database.
    """

    template_name='work.html'

    def get(self, request, *args, **kwargs):
        
        try:
            current= float(request.GET.get("current"))
            voltage = float(request.GET.get("voltage"))
            instalation = str(request.GET.get("instalation"))
            material = str(request.GET.get("material"))
            nmproy = str(request.GET.get("nmproy"))
        
        except TypeError:
            return redirect('/accounts/login/')
        
        except ValueError:
            return render(request, "home.html",{
                'error_message':f'¡Incorrecto!',
                'help_message':'Ingrese los valores Correctante'
            })
        
        list_user_proy = request.GET.get("list_user_proy")
        if nmproy not in list_user_proy:
            return render(request, "home.html",{
                'error_message':f'¡Acceso Denegado!',
                'help_message':'El Usuario no ha sido ingresado al proyecto'
            })

        date_select = timezone.now()
        #All-TypeProyects (for specific "mproy") Where The User has Permissions
        typroy =  list(Proyect.objects.filter(user=request.user.id,nmproy=nmproy).values_list('typroy',flat=True).distinct())
        
        """Ampacity() Takes the actual "current" value and modifies it according to the parameters
        Returns: ampacity 
        """
        ampacity = float(Ampacity(current))
        
        """QuerySelect() Takes the actual "material"/"ampacity" values to find new_current
        Returns: new_current 
        """
        new_current = int(QuerySelect(material,ampacity).new_current)
        
        context = self.get_context_data(**kwargs)
        context={
            'current':current,
            'voltage':voltage,
            'ampacity':ampacity,
            'new_current':new_current,          
            'instalation':instalation,
            'material':material,
            'nmproy':nmproy,
            'typroy':typroy,
            'date_select':date_select.strftime("%Y-%m-%d %H:%M")
        }

        return self.render_to_response(context)
    
    
class Saveresults(HomeLogin):
    
    """
    Gets the information from the form and creates a new entry in the database 
    with the name of the file and all the information from the user's job.
    If a file with the same name is found, it will add the creation date to the end of the line.
    """

    def get(self, request, *args, **kwargs):

        savename = str(request.GET.get("savename"))
                
        username = str(request.GET.get('username'))
        nmproy = str(request.GET.get('nmproy'))
        
        current= float(request.GET.get("current"))
        voltage = float(request.GET.get('voltage'))
        ampacity = float(request.GET.get('ampacity'))
        new_current = float(request.GET.get('new_current'))

        message = str(request.GET.get('message'))
        
        date_select = datetime.strptime(request.GET.get('date_select'), '%Y-%m-%d %H:%M')

        list_savename = list(SavesProyects.objects.values_list('savename',flat=True))
        if savename in list_savename:
            savename = f'{savename} [{date_select.strftime("%Y-%m-%d")}]'
        
        SavesProyects.objects.create(
            savename = savename,
            username = username,
            nmproy = nmproy,
            current= current,
            voltage = voltage,
            ampacity = ampacity,
            new_current = new_current,
            message = message,
            datenow = date_select
            )
        
        return render(request, "work.html",{
            'succes_message':f'¡Guardado!',
            'help_message':'Seleccion guardada Correctamente'
        })