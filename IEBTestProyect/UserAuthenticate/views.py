from django.views.generic.base import TemplateView
from .models import Usuario, Proyect


class HomeLogin(TemplateView):
    template_name='home.html'

    def get(self, request, *args, **kwargs):
        user = request.user.id
        info = Usuario.objects.get(id=user)
        list_nmproy = list(Proyect.objects.values_list('nmproy',flat=True))
 
        context = self.get_context_data(**kwargs)
        context={
            'email':info.email,
            'name':info.first_name,
            'lastname':info.last_name,
            'IsActive':info.is_active,
            'list_nmproy':list_nmproy
        }
        return self.render_to_response(context)
