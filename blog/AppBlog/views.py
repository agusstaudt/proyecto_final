from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Interesado
from AppBlog.forms import InteresadoFormulario
# Create your views here.
def inicio(request):
    return render(request, "AppBlog/index.html")

def usuario(request):
    return HttpResponse("Vista usuario")

def interesadoFormulario(request):
    if request.method == "POST":
        miFormulario = InteresadoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Interesado(nombre=informacion["nombre"], 
                               apellido=informacion["apellido"], 
                               email=informacion["email"], 
                               organizacion=informacion["organizacion"], 
                               cuit=informacion["cuit"])
            curso.save()
            return render(request, "AppBlog/index.html")
    else:
        miFormulario = InteresadoFormulario()
    return render(request, "AppBlog/interesadoFormulario.html", {"miFormulario": miFormulario})