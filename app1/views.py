from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Usuario
from .forms import UsuarioForm
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

# def update(request, pk):    
#     usuario = get_object_or_404(Usuario, pk=pk)
#     if request.method == 'POST':
#         form = UsuarioForm(request.POST, instance=usuario)
#         if form.is_valid():            
#             form.save()
#             return redirect('mostrar')
#     else:
#         form = UsuarioForm(instance=usuario)
    
#     return render(request, 'editar.html', {'form': form, 'usuario': usuario})


def update(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('mostrar')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'editar.html', {'form': form, 'usuario': usuario})

def destroy(request, id ):  
    usuario = Usuario.objects.get(id=id)  
    usuario.delete()  
    return redirect("mostrar") 

def crear_registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar')
    else:
        form = UsuarioForm()
    return render(request, 'crear_registro.html', {'form': form})

def edit(request, id):  
    usuario = Usuario.objects.get(id=id)  
    return render(request,'editar.html', {'usuario':usuario})  

def mostrar_usuarios(request):
    usuarios = Usuario.objects.all() # Obtén todos los usuarios de la base de datos
    context = {'usuarios': usuarios} # Crea un diccionario con los datos de los usuarios
    return render(request, 'mostrar.html', context)

def lista_registros(request):
    registros_tabla1 = Tabla1.objects.all()
    registros_tabla2 = Tabla2.objects.all()
    registros_tabla3 = Tabla3.objects.all()

    context = {
        'registros_tabla1': registros_tabla1,
        'registros_tabla2': registros_tabla2,
        'registros_tabla3': registros_tabla3
    }