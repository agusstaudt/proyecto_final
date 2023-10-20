from django.urls import path
from AppBlog import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('usuario/', views.usuario, name="Usuario"),
    path('interesado/', views.interesadoFormulario, name="Interesado")
]