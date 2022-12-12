from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class HomeLogin(TemplateView):
    template_name='home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeLogin, self).get_context_data(*args, **kwargs)
        context={
            'nombre': "Aqui Va el Email",
            'message1': "email"   
        }

        return context