from email import message
from pyexpat.errors import messages
from django.forms import PasswordInput
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
import random
from tienda.models import Categorias, Marca, Producto
from .forms import contactoForms,CustomUserCreationForm,ProductoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import Http404




from .serializers import productoSerializer
from rest_framework import viewsets


from django.db.models import Q



class ProductoViewSet(viewsets.ModelViewSet):
    queryset =Producto.objects.all()
    serializer_class = productoSerializer




def home(request):
    return render(request, 'home.html', {'name': 'gvrrido'})




def store(request):
    busqueda = request.POST.get("buscador")
    productos = Producto.objects.order_by('nombre')
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    try:
        productos = productos
    except:
        raise Http404

    data = {'entity': productos,
            'title': 'LISTADO DE PRODUCTOS',
            }
    return render(request,'store.html', data)
    
    
def contacto(request):
    data = {
        'form': contactoForms()
        

    }
    if request.method == 'POST':
        formulario = contactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data ["form"] = formulario
    return render(request, 'contacto.html', data )


    
def detalleProducto(request,id):
    producto = get_object_or_404(Producto,id=id)
    context = {
        'producto': producto
    }
    return render(request, 'producto/detalle.html', context )




def registro(request):  
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'post':
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login (request,user)
            messages.success(request, "Usurio Registrado!")
            return redirect(to='home')
        data ["form"] = formulario
    return render(request, 'registration/registro.html', data )



##################################################################################################################################################### VIEW PRODUCTO    #############################################################################



def addProducto(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/listar")
        else:
            data["form"] = formulario   
    return render(request, 'producto/agregar.html', data)


def listarProductos(request):
    busqueda = request.POST.get("buscador")
    lista_productos = Producto.objects.order_by('nombre')
    if busqueda:
        lista_productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    try:
        lista_productos = lista_productos
    except:
        raise Http404

    data = {'entity': lista_productos,
            'title': 'LISTADO DE PRODUCTOS',
            }
    return render(request, 'producto/listar.html', data)





    
    