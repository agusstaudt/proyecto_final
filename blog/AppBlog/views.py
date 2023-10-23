from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Interesado, Taller ,InteresadoTalleres
from AppBlog.forms import InteresadoFormulario, InteresadoTall, BuscaTallerForm
# Create your views here.
def inicio(request):
    return render(request, "AppBlog/index.html")

def usuario(request):
    return HttpResponse("Vista usuario")
# definimos formulario de interesados en los servicios del blog
## servicio de consultoria
def interesadoFormulario(request):
    if request.method == "POST":
        miFormulario = InteresadoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            interest = Interesado(nombre=informacion["nombre"], 
                               apellido=informacion["apellido"], 
                               email=informacion["email"], 
                               organizacion=informacion["organizacion"], 
                               cuit=informacion["cuit"],
                               servicio=informacion["servicio"])
            interest.save()
            return render(request, "AppBlog/index.html")
    else:
        miFormulario = InteresadoFormulario()
    return render(request, "AppBlog/interesadoFormulario.html", {"miFormulario": miFormulario})

# Busqueda de comision de talleres
def buscar(request):
        if request.method == "POST":
            miFormulario = BuscaTallerForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data

                print(f'\n\n Contenido cleaned: {informacion} \n\n')

                talleres = Taller.objects.filter(taller__icontains=informacion['taller'])
             
                return render(request, "AppBlog/resultadoBusquedaComision.html", {"talleres":talleres})
        else:
            miFormulario = BuscaTallerForm()
        return render(request, "AppBlog/busquedaComision.html", {"miFormulario": miFormulario})

def mostrar(request):
    pass

## talleres disponibles
def interesadoTalleres(request):
    if request.method == "POST":
        miFormularioTalleres = InteresadoTalleres(request.POST) # Aqui me llega la informacion del html
        print(miFormularioTalleres)
        if miFormularioTalleres.is_valid():
            informacionTalleres = miFormularioTalleres.cleaned_data
            interest = InteresadoTall(nombre=informacionTalleres["nombre"], 
                                     taller=informacionTalleres["taller"])
            interest.save()
            return render(request, "AppBlog/index.html")
    else:
        miFormularioTalleres = InteresadoTall()
    return render(request, "AppBlog/interesadosTalleres.html", {"miFormularioTalleres": miFormularioTalleres})

# CRUD 
## lectura de interesados
def leerInteresados(request):
      interesados = Interesado.objects.all() #trae todos los profesores
      contexto= {"interesados":interesados} 
      return render(request, "AppBlog/leerInteresados.html",contexto)
## eliminar interesados
def eliminarInteresado(request, interesado_id):

    interesados = Interesado.objects.get(id=int(interesado_id))
    interesados.delete()
    # vuelvo al menú
    interesados = Interesado.objects.all() # trae todos los profesores

    contexto = {"interesados": interesados}

    return leerInteresados(request)
## editar interesados
def editInteresado(request, interesado_id):
    if request.method == "POST":
        miFormulario = InteresadoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                interest = Interesado(nombre=informacion["nombre"], 
                                    apellido=informacion["apellido"], 
                                    email=informacion["email"], 
                                    organizacion=informacion["organizacion"], 
                                    cuit=informacion["cuit"],
                                    servicio=informacion["servicio"])
                interest.save()
                return render(request, "AppBlog/index.html")
    else:
        miFormulario = InteresadoFormulario()
    return render(request, "AppBlog/interesadoFormulario.html", {"miFormulario": miFormulario})
