from django import forms
class InteresadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    organizacion = forms.CharField(max_length=40)
    cuit = forms.CharField(max_length=40)

class ConsultoriaForm(forms.Form):
    servicio = forms.CharField(max_length=40)
