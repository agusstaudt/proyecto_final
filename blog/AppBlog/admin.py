from django.contrib import admin
from .models import Usuario, Interesado, InteresadoTalleres, Taller, TallerBase, IncripcionTaller

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Interesado)
admin.site.register(InteresadoTalleres)
admin.site.register(Taller)
admin.site.register(TallerBase)
admin.site.register(IncripcionTaller)
