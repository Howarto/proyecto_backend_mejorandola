# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext
from models import *
from forms import * 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

def home(request):
    categorias = Categoria.objects.all()
    proyectos = Proyecto.objects.all()
    template = "home.html"
    return render(request, template,{"categorias" : categorias, "proyectos":proyectos, "request":request})

def account(request):
    template = "account.html"
    return render(request, template,locals())

class ProyectoListView(ListView):
    model = Proyecto
    context_object_name = 'proyectos'
    def get_template_names(self):
        return 'proyectos.html'

class ProyectoDetailView(DetailView):
    model = Proyecto
    context_object_name = 'proyecto'
    def get_template_names(self):
        return 'proyectos_detail.html'

@login_required
def minus(request,proyecto_id):
    proyecto = get_object_or_404(Proyecto,pk=proyecto_id)
    proyecto.votos = proyecto.votos - 1
    proyecto.save()
    return HttpResponseRedirect("/")

@login_required
def plus(request,proyecto_id):
    proyecto = get_object_or_404(Proyecto,pk=proyecto_id)
    proyecto.votos = proyecto.votos + 1
    proyecto.save()
    return HttpResponseRedirect("/")
