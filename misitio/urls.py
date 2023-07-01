from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.peli, name="peli"),
    path('dracula/', views.dracula, name="dracula"),
    path('elc/', views.elc, name="esperandolacarroza"),
    path('ipf/', views.ipf, name="Iluminados por el fuego"),
    path('psvl/', views.psvl, name="Papa se volvio loco"),
    path('lbmldm/', views.lbmldm, name="Los Bañeros Mas Locos Del Mundo"),
    path('st/', views.st, name="Starship Troopers"),
    path('editar/<int:id>/', views.edit, name="editar"),
    #path('editar/<int:id>/', views.update, name="editar"),
    path('destroy/<int:id>/', views.destroy, name="eliminar"),
    path('update/<int:id>/', views.update, name="actualizar"),
    path('mostrar/', views.mostrar_usuarios, name='mostrar'),
    path('lista_registros/', views.lista_registros, name='lista_registros'),
    path('crear_registro/', views.crear_registro, name='crear_registro'),
]
