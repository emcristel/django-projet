from django.shortcuts import render, redirect
from .forms import TableForm
from .forms import ArchitecteForm
from . import models
from .models import Table
from .models import Architecte
from django.http import HttpResponseRedirect
from django import forms


def home(request):
    return render(request, 'archi/index.html')


def ajout(request):
    if request.method=="POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Tous")
        else:
            form = TableForm
            return render(request,'archi/ajout.html',{"form": form})

    else:
        form = TableForm()
        return render(request, 'archi/ajout.html',{"form" : form})


def traitement(request):
    oform = TableForm(request.POST)
    if oform.is_valid():
        oeuvre = oform.save()
        return HttpResponseRedirect(request, "/archi/")
    else:
        return render(request, "archi/ajout.html")



def update(request, id):
    oeuvre = Table.objects.get(pk=id)
    form = TableForm(request.POST or None, instance=oeuvre)
    if form.is_valid():
        form.save()
        return redirect("Tous")
    return render(request, 'archi/update.html', {'oeuvre':oeuvre, 'form':form} )


def delete(request, id):
    oeuvre= models.Table.objects.get(pk=id)
    oeuvre.delete()
    return redirect("Tous")

def tous (request):
    oeuvre= list(models.Table.objects.all())
    return render(request, 'archi/tous.html',{'oeuvre':oeuvre})


def ajout_architecte(request):
    submitted = False
    if request.method == 'POST':
        form = ArchitecteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Architecte')
    else:
        form = ArchitecteForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'archi/ajout_architecte.html', {'form':form, 'submitted':submitted})

def liste_architecte(request):
   liste_architecte = Architecte.objects.all()
   return render(request, 'archi/liste_architecte.html', {'liste_architecte': liste_architecte})

def update_architecte(request, architecte_id):
    architecte = Architecte.objects.get(pk=architecte_id)
    form = ArchitecteForm(request.POST or None, instance=architecte)
    if form.is_valid():
        form.save()
        return redirect("Architecte")
    return render(request, 'archi/update_architecte.html', {'architecte':architecte, 'form':form} )

def delete_architecte(request, architecte_id):
    architecte = Architecte.objects.get(pk=architecte_id)
    architecte.delete()
    return redirect('Architecte')

