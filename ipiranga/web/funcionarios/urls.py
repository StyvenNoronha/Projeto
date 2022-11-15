
from django.urls import path, include
from funcionarios import views
urlpatterns = [

    path('',views.cad, name='cad' ),
    path('lis/',views.lista, name='lista'),
    path('lis/<int:pk>',views.lista, name='lista'),
    path('cargo/',views.cargo, name='car'),
    path('pdf/',views.listapdf, name='pdf'),

]
