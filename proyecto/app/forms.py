from django import forms
from django.forms import ModelForm
from models import *

class ProyectoForm(ModelForm):
    
    class Meta:
        model = Proyecto
        exclude = ("comentarios", "votos", "participantes")

        
class ComentarioForm(ModelForm):
    
    class Meta:
        model = Comentario
        exclude = ("user",)
        