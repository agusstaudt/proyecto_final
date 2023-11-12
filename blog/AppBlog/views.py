from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from AppBlog.models import *
from AppBlog.forms import *
# to login, registar and log out
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# funcion login 
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            nombre_usuario = authenticate(username=usuario, password=clave)

            if nombre_usuario is not None:
                login(request, nombre_usuario)

                return render(request, "AppBlog/indexGetIn.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                form = AuthenticationForm()
                return render(request, "AppBlog/index.html", {"mensaje":"Datos incorrectos", 'form':form})
           
        else:

            return render(request, "AppBlog/index.html", {"mensaje":"Usuario y/o contraseña incorrecto"})

    form = AuthenticationForm() # crea el formulario

    return render(request, "AppBlog/login.html", {"form": form})

# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppBlog/indexGetIn.html" ,  {"mensaje":f"Usuario Creado. Bienvenido {username} :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppBlog/registro.html" ,  {"form":form})

# Create your views here.
def inicio(request):
    return render(request, "AppBlog/index.html")

def usuario(request):
    return HttpResponse("Vista usuario")
# definimos formulario de interesados en los servicios del blog
## servicio de consultoria
@login_required
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
## cambiar el link en reservar un demo para que lleve a un html con ambos links, de interesado para consultoria e interesado para taller

############ clases basadas en vistas
class TallerListView(LoginRequiredMixin, ListView):
    model = Taller
    template_name = "AppBlog/listaTalleresUsuario.html"

class TallerDetailView(DetailView):
    model = Taller
    template_name = "AppBlog/tallerDetalle.html"

class TallerCreateView(CreateView):
    model = Taller
    template_name = "AppBlog/taller_form.html"
    success_url = reverse_lazy("Lista")
    fields = ['taller', 'comision']

class TallerUpdateView(UpdateView):
    model = Taller
    template_name = "AppBlog/taller_edit.html"
    success_url = reverse_lazy("Lista")
    fields = ['taller', 'comision']

class TallerDeleteView(DeleteView):
    model = Taller
    template_name = "AppBlog/taller_confirm_delete.html"
    success_url = reverse_lazy("Lista")
    
### Inscripción a un taller
def inscribirse_curso(request):
    return render(request, 'AppBlog/index.html')

def confirmar_inscripcion(request, nombre_taller):
    taller = get_object_or_404(TallerBase, nombre=nombre_taller)

    if request.method == 'POST':
        form = IncripcionTallerForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre']
            inscripcion = IncripcionTaller(nombre=nombre_usuario, taller=taller)
            inscripcion.save()
            return render(request, 'AppBlog/inscripcionExitosa.html', {'nombre': nombre_usuario, 'taller': taller})
    else:
        form = IncripcionTallerForm()

    return render(request, 'AppBlog/confirmarInscripcion.html', {'taller': taller, 'form': form})
