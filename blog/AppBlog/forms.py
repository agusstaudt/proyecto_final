from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InteresadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    organizacion = forms.CharField(max_length=40)
    cuit = forms.CharField(max_length=40)
    servicio = forms.CharField(max_length=40)

class InteresadoTall(forms.Form):
    nombre = forms.CharField(max_length=40)
    taller = forms.CharField(max_length=20)

class InteresadoTallerForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    
class BuscaTallerForm(forms.Form):
    taller = forms.CharField(max_length=40)

class TallerForm(forms.Form):
    taller = forms.CharField(max_length=40)
    comision = forms.CharField(max_length=20)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

# inscripcion a taller
class IncripcionTallerForm(forms.Form):
    nombre = forms.CharField(max_length=40)