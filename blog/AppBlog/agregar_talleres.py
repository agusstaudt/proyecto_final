# agregar_talleres.py
from django.core.management.base import BaseCommand
from AppBlog.models import TallerBase

class Command(BaseCommand):
    help = 'Agrega talleres a la base de datos'

    def handle(self, *args, **kwargs):
        talleres = ['Desarrollo Web', 'Python Intemedio', 'Ciencia de Datos', 'Estadística Aplicada',
                    'Evaluación de Impacto de Políticas Públicas', 'Data Analytics']
        for nombre_taller in talleres:
            TallerBase.objects.create(nombre=nombre_taller)
        self.stdout.write(self.style.SUCCESS('Talleres agregados exitosamente'))
