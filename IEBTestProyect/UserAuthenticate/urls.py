from django.urls import path, include
from .views import HomeLogin

urlpatterns = [

    path("accounts/", include("django.contrib.auth.urls")),
    path('', HomeLogin.as_view(), name='home'),
]
