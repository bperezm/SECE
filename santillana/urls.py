from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('certificacion/', views.certificacion, name="certificacion"),
    path('estandares/', views.estandares, name="estandares"),
]
