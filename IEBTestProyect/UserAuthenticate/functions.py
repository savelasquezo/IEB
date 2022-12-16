from .models import Usuario, Proyect, Wireline

def GlobalContext(request):
    if request.user.id is not None:
        user = request.user.id
        info_user = Usuario.objects.get(id=user)
        
        #All-Proyects (nmproy) Where The User has Permissions
        list_user_proy = list(Proyect.objects.filter(user=user).values_list('nmproy',flat=True).distinct())
        
        return {
            'email':info_user.email,
            'name':info_user.first_name,
            'lastname':info_user.last_name,
            'IsActive':info_user.is_active,
            'valid_nmproy':list_user_proy
            }
    return {}   

def Ampacity(current):
    if current < 40:
        ampacity= 1.26
    else:
        ampacity= 2.50
    return ampacity

def QuerySelect(material,ampacity):
    new_current = Wireline.objects.filter(material=material,ampacity=ampacity).first().new_current
    return new_current

