from django import forms
from django.forms import ModelForm
from models import *

class ComentarioForm(ModelForm):
    
    class Meta:
        model = Comentario
        
class ComentarioForm(ModelForm):
    
    class Meta:
        model = Comentario
        exclude = ("user",)
        