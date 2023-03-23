from django.shortcuts import render
from .models import Carros
from django.shortcuts import redirect

def home(request):
    carros = Carros.objects.all()
    return render(request, 'index.html', {'carros': carros})

def salvar(request):
    name = request.POST.get('name')
    Carros.objects.create(name=name)
    carros = Carros.objects.all()
    return render(request, 'index.html', {'carros': carros})

def editar(request,id):
    carros = Carros.objects.get(id=id)
    return render(request, 'update.html', {'carros': carros})

def update(request,id):
    carros = Carros.objects.get(id=id)
    vname = request.POST.get('name')
    carros.name = vname
    carros.save()
    return redirect(home)

def deletar(request,id):
    carros = Carros.objects.get(id=id)
    carros.delete()
    return redirect(home)