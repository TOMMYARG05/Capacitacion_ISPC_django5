from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioForm#, CrearRegistroForm
from .models import Tabla1 , Tabla2 , Tabla3


 
# Create your views here.
def dracula(request): 
    return render(request, 'dracula.html')

def elc(request):
    return render(request, 'EsperandolaCarroza.html')

def ipf(request):
    return render(request, 'Iluminadosporelfuego.html' )

def psvl(request):
    return render(request, 'papasevolvioloco.html')

def lbmldm(request):
    return render(request,'losbañerosmaslocosdelmundo.html')

def st(request):
    return render(request, 'Starshiptroopers.html')

def peli(request):
    return render(request,'peli.html')

def mostrar(request):
    return render(request, 'mostrar.html')
 
def login(request):  
    usuarios = Usuario.objects.all()  
    return render(request,"login.html",{'usuarios':usuarios})  
 
def edit(request, id):  
    usuario = Usuario.objects.get(id=id)  
    return render(request,'edit.html', {'usuario':usuario})  
 
def update(request, id):  
    usuario = Usuario.objects.get(id=id)  
    form = Usuario(request.POST, instance = usuario)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'usuario': usuario})  
     
def destroy(request, id):  
    usuario = Usuario.objects.get(id=id)  
    usuario.delete()  
    return redirect("/") 

def crear_registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = UsuarioForm()

    return render(request, 'crear_registro.html', {'form': form})

def lista_registros(request):
    registros_tabla1 = Tabla1.objects.all()
    registros_tabla2 = Tabla2.objects.all()
    registros_tabla3 = Tabla3.objects.all()

    context = {
        'registros_tabla1': registros_tabla1,
        'registros_tabla2': registros_tabla2,
        'registros_tabla3': registros_tabla3
    }

    return render(request, 'lista_registros.html', context)

def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtén todos los usuarios de la base de datos
    context = {'usuarios': usuarios}  # Crea un diccionario con los datos de los usuarios
    return render(request, 'mostrar.html', context)


# def crear_registro(request):
#     if request.method == 'POST':
#         campo1 = request.POST.get('campo1')
#         campo2 = request.POST.get('campo2')
#         campo3 = request.POST.get('campo3')

#         registro_tabla1 = Tabla1(campo1=campo1, campo2=campo2 , campo3=campo3)
#         registro_tabla1.save()
#         registro_tabla2 = Tabla2(campo1=campo1, campo2=campo2, campo3=campo3)
#         registro_tabla2.save()
#         registro_tabla3 = Tabla3(campo1=campo1, campo2=campo2, campo3=campo3)
#         registro_tabla3.save()

#         return redirect('lista_registros')
#     else:
#         return render(request, 'crear_registro.html')
    
# def lista_registros(request):
#     registros_tabla1 = Tabla1.objects.all()
#     registros_tabla2 = Tabla2.objects.all()
#     registros_tabla3 = Tabla3.objects.all()

#     context = {
#         'registros_tabla1': registros_tabla1,
#         'registros_tabla2': registros_tabla2,
#         'registros_tabla3': registros_tabla3
#     }

#     return render(request, 'lista_registros.html', context)