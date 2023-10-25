from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Interesado, Taller ,InteresadoTalleres
from AppBlog.forms import InteresadoFormulario, InteresadoTall, BuscaTallerForm, TallerForm
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
             
                return render(request, "AppBlog/resultadoBusquedaTaller.html", {"talleres":talleres})
        else:
            miFormulario = BuscaTallerForm()
        return render(request, "AppBlog/busquedaTaller.html", {"miFormulario": miFormulario})

def mostrar(request):
    pass

## talleres disponibles
def interesadoTalleres(request):
    if request.method == "POST":
        miFormularioTalleres = InteresadoTall(request.POST) # Aqui me llega la informacion del html
        print(miFormularioTalleres)
        if miFormularioTalleres.is_valid():
            informacionTalleres = miFormularioTalleres.cleaned_data
            interest = InteresadoTalleres(nombre=informacionTalleres["nombre"], 
                                          taller=informacionTalleres["taller"])
            interest.save()
            return render(request, "AppBlog/index.html")
    else:
        miFormularioTalleres = InteresadoTall()
    return render(request, "AppBlog/interesadosTalleres.html", {"miFormularioTalleres": miFormularioTalleres})

## agregar taller 
def agregarTaller(request):
    if request.method == "POST":
        miFormulario = TallerForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            interest = Taller(taller=informacion["taller"], 
                              comision=informacion["comision"])
            interest.save()
            return render(request, "AppBlog/index.html")
    else:
        miFormulario = TallerForm()
    return render(request, "AppBlog/talleresFormulario.html", {"miFormulario": miFormulario})
# CRUD 
## lectura de talleres
def leerTalleres(request):
      talleres = Taller.objects.all() #trae todos los profesores
      contexto= {"talleres":talleres} 
      return render(request, "AppBlog/leerTalleres.html",contexto)
### eliminar talleres (da partir de la view de lectura de talleres se puede eliminar)
def eliminarTalleres(request, taller_id):

    talleres = Taller.objects.get(id=int(taller_id))
    talleres.delete()
    # vuelvo al menú
    talleres = Taller.objects.all() # trae todos los profesores

    contexto = {"talleres": talleres}

    return leerTalleres(request)
## editar talleres (da partir de la view de lectura de talleres se pueden editar talleres)
def editTaller(request, taller_id):
    if request.method == "POST":
        miFormulario = TallerForm(request.POST) # Aqui me llega la informacion del html
        
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                taller = Taller.objects.get(id=taller_id)
                taller.taller = informacion['taller']
                taller.comision = informacion['comision']
                taller.save()
                return render(request, "AppBlog/index.html")
    else:
        taller = Taller.objects.get(id=taller_id)
        miFormulario = TallerForm(initial={'taller': taller.taller})
    return render(request, "AppBlog/interesadosTalleres.html", {"miFormularioTalleres": miFormulario})
# seguir video en 1:16
## cambiar el link en reservar un demo para que lleve a un html con ambos links, de interesado para consultoria e interesado para taller
