from django.urls import path, include
from .views import HomeLogin, Workresults, Saveresults

urlpatterns = [

    path("accounts/", include("django.contrib.auth.urls")),
    path('', HomeLogin.as_view(), name='ieb'),
    path('work/', Workresults.as_view(), name='work'),
    path('work/save/', Saveresults.as_view(), name='save'),
]
