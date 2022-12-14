from django.urls import path, include
from .views import HomeLogin

"""django.contrib.auth.urls Genric Templates for accounts Login/Logout/Password
    Verificaingreso()---->Integrado Django AuthenticateSystem
"""

urlpatterns = [

    path("accounts/", include("django.contrib.auth.urls")),
    path('', HomeLogin.as_view(), name='ieb'),
]
