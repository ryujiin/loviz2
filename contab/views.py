from django.shortcuts import render,render_to_response
from models import *
from forms import * 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

# Create your views here.
@login_required
def home(request):
	template='base.html'
	return render(request, template,{"request":request})

@login_required
def materiales(request):
    datos_tablas=["Nombre","Precio x Unidad",]
    materiales=Material.objects.all().order_by('-pk')
    template='mate.html'
    return render(request,template,{"materiales":materiales,"datos_tablas":datos_tablas,"request":request})

@login_required
def add_material(request):
    if request.POST:
        form = MaterialAddForm(request.POST)
        if form.is_valid():
            name_m=form.cleaned_data['nombre']
            material = form.save()
            n_material=Material.objects.filter(nombre=name_m)[0]
            unid_compra=n_material.unidad_de_compra
            n_stock=Stock(material=n_material,unidad_compra=unid_compra)
            n_stock.save()
            return HttpResponseRedirect("/contab/materiales/")
    else:
        form=MaterialAddForm()

    template="forms/add_material.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required
def compras(request):
    datos_tablas = ["material","cantidad","fecha","Soles"]
    compras=Compra.objects.all().order_by('-pk')
    template='compras.html'
    return render(request,template,{"compras":compras,"datos_tablas":datos_tablas,"request":request})

@login_required
def add_compras(request):
    if request.POST:
        form =ComprasForm(request.POST)
        if form.is_valid():
            compra = form.save(commit = False)
            name_m=form.cleaned_data['material']
            cantidad_m=form.cleaned_data['cantidad']
            name_m=Material.objects.filter(nombre=name_m)[0]
            precio=name_m.precio_por_unidad
            compra.soles_comprados = form.cleaned_data['cantidad']*precio
            compra.save()
            a_stock=Stock.objects.filter(material=name_m).order_by("-pk")[0]
            total_cantidad=a_stock.cantidad+cantidad_m
            total_soles=a_stock.total_soles+precio
            n_stock=Stock(material=name_m,cantidad=cantidad_m,total_cant=total_cantidad,total_soles=total_soles)
            n_stock.save()
            return HttpResponseRedirect("/contab/compras/")
    else:
        form=ComprasForm()

    template="forms/add_material.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))