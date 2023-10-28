from django.urls import path
from AppBlog import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('usuario/', views.usuario, name="Usuario"),
    path('interesado/', views.interesadoFormulario, name="Interesado"),
    path('agregarTalleres', views.agregarTaller, name = "AgregarTalleres"),
    path('leerTalleres', views.leerTalleres, name = "LeerTalleres"),
    path('interesTalleres', views.interesadoTalleres, name = "InteresTalleres"),
    path('buscar/', views.buscar, name = "Buscar"),
    path('mostrar/', views.mostrar, name = 'Mostrar'),
    path('eliminarTalleres/<int:taller_id>/', views.eliminarTalleres, name="EliminarTalleres"),
    path('editarTaller/<int:taller_id>/', views.editTaller, name="EditarTaller")
]

# URL's basadas en clases
urlpatterns += [
    path('clases/lista/', views.TallerListView.as_view(), name="Lista"),
    path('clases/detalle/<int:pk>/', views.TallerDetailView.as_view(), name="Detalles"),
    path('clases/nuevo/', views.TallerCreateView.as_view(), name="Nuevo"),
    path('clases/editar/<int:pk>/', views.TallerUpdateView.as_view(), name="Editar"),
    path('clases/eliminar/<int:pk>/', views.TallerDeleteView.as_view(), name="Eliminar"),
]
