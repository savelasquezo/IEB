from .models import Usuario, Proyect, Wireline

def GlobalContext(request):
    
    """
    Generates a global context with basic user information for use by all views of the project.
    "IEBTestProyect/settings.py"
    TEMPLATES = [{'OPTIONS': {'context_processors': ['UserAuthenticate.functions.GlobalContext',],},},]
    """
    
    
    if request.user.id is not None:
        user = request.user.id
        info_user = Usuario.objects.get(id=user)

        list_material = list(Wireline.objects.values_list('material',flat=True).distinct())
        list_nmproy = list(Proyect.objects.values_list('nmproy',flat=True).distinct())

        #All-Proyects (nmproy) Where The User has Permissions
        list_user_proy = list(Proyect.objects.filter(user=request.user.id).values_list('nmproy',flat=True).distinct())
        
        return {
            'username':info_user.username,
            'email':info_user.email,
            'name':info_user.first_name,
            'lastname':info_user.last_name,
            'IsActive':info_user.is_active,
            'list_user_proy':list_user_proy,
            'list_material':list_material,
            'list_nmproy':list_nmproy
            }
    return {}   

def Ampacity(current):
    if current < 40:
        ampacity= 1.26
    else:
        ampacity= 2.50
    return ampacity

def QuerySelect(material,ampacity):
    WireLineSelect = Wireline.objects.filter(material=material,ampacity=ampacity).first()
    return WireLineSelect

