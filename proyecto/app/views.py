# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext
from models import *
from forms import * 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home(request):
    categorias = Categoria.objects.all()
    template = "index.html"
    return render(request, template,{"categorias" : categorias, "enlaces":enlaces, "request":request})

def categoria(request,id_categoria):
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria,pk = id_categoria)
    #cat = Categoria.objects.get(pk = id_categoria)
    enlaces = Enlace.objects.filter(categoria = cat)
    template = "index.html"
    return render(request, template,locals())

# @login_required
# def minus(request,enlace_id):
#     enlace = get_object_or_404(Enlace,pk=enlace_id)
#     enlace.votos = enlace.votos - 1
#     enlace.save()
#     return HttpResponseRedirect("/")

# @login_required
# def plus(request,enlace_id):
#     enlace = get_object_or_404(Enlace,pk=enlace_id)
#     enlace.votos = enlace.votos + 1
#     enlace.save()
#     return HttpResponseRedirect("/")

@login_required
def add(request):
    if request.POST:
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit = False)
            proyecto.save()
            return HttpResponseRedirect("/")
    else:
        form = ProyectoForm()
    template = "signin.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

def signin(request):
    template = "signin.html"
    return render(request, template,locals())