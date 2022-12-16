from datetime import datetime

from django.views.generic.base import TemplateView
from django.utils import timezone

from .models import Proyect, Wireline, SavesProyects
from .functions import Ampacity, QuerySelect


class HomeLogin(TemplateView):
    template_name='home.html'
    
    def get(self, request, *args, **kwargs):

        list_material = list(Wireline.objects.values_list('material',flat=True).distinct())
        list_nmproy = list(Proyect.objects.values_list('nmproy',flat=True).distinct())
 
        context = self.get_context_data(**kwargs)
        context={
            'list_material':list_material,
            'list_nmproy':list_nmproy
        }
        return self.render_to_response(context)

class Workresults(HomeLogin):
    
    template_name='work.html'

    def get(self, request, *args, **kwargs):

        current= float(request.GET.get("current"))
        voltage = float(request.GET.get("voltage"))
        instalation = str(request.GET.get("instalation"))
        material = str(request.GET.get("material"))
        nmproy = str(request.GET.get("nmproy"))
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
        new_current = int(QuerySelect(material,ampacity))
        
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

    template_name='save.html'
    
    def get(self, request, *args, **kwargs):

        savename = str(request.GET.get("savename"))
        username = str(request.GET.get('username'))
        nmproy = str(request.GET.get('nmproy'))
        
        current= float(request.GET.get("current"))
        voltage = float(request.GET.get('voltage'))
        ampacity = float(request.GET.get('ampacity'))
        new_current = float(request.GET.get('new_current'))
        date_select = datetime.strptime(request.GET.get('date_select'), '%Y-%m-%d %H:%M')

        
        SavesProyects.objects.create(
            savename = savename,
            username = username,
            nmproy = nmproy,
            current= current,
            voltage = voltage,
            ampacity = ampacity,
            new_current = new_current,
            datenow = date_select
            )
        
        context = self.get_context_data(**kwargs)
        context={
            'IsSave':True
        }

        return self.render_to_response(context)
    