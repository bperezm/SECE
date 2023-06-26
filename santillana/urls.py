from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('certificacion/', views.certificacion, name="certificacion"),
    path('estandares/', views.estandares, name="estandares"),
    path('conocer/', views.conocer, name="conocer"),
    path('informacion/', views.informacion, name="informacion"),
    path('etica/', views.etica, name="etica"),
    path('contacto/', views.contacto, name="contacto"),
    path('aviso-privacidad/', views.aviso, name="aviso"),
    path('condiciones-de-uso/', views.condiciones, name="condiciones"),
]
