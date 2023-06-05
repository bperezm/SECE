from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('certificacion/', views.certificacion, name="certificacion"), # Terminar
    path('estandares/', views.estandares, name="estandares"), #Refactorizar
    path('conocer/', views.conocer, name="conocer"), #Refactorizar
    path('informacion/', views.informacion, name="informacion"), #Lista
    path('etica/', views.etica, name="etica"),#Lista
    path('contacto/', views.contacto, name="contacto"), #Revisar Formulario
]
