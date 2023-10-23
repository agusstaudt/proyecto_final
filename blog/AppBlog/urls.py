from django.urls import path
from AppBlog import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('usuario/', views.usuario, name="Usuario"),
    path('interesado/', views.interesadoFormulario, name="Interesado"),
    path('leerInteresados', views.leerInteresados, name = "LeerInteresados"),
    path('talleres', views.interesadoTalleres, name = "Talleres"),
    path('buscar/', views.buscar, name = "Buscar"),
    path('mostrar/', views.mostrar, name = 'Mostrar'),
    path('eliminarInteresado/<int:interesado_id>/', views.eliminarInteresado, name="EliminarInteresado"),
    path('editInteresado/<int:interesado_id>/', views.editInteresado, name="EditInteresado")
]