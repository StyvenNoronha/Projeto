from django.urls import path, include
from manu import views


urlpatterns = [

    path('',views.manutencao, name='manu'),
    path('motor/',views.cadmotor, name='motor'),
    path('listamanu/',views.lismanu, name='listmanu'),

]