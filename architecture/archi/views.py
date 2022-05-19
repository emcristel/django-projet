from django.shortcuts import render, redirect
from .forms import OeuvreForm
from .forms import ArchitecteForm
from . import models
from .models import Oeuvre
from .models import Architecte
from django.http import HttpResponseRedirect
from django import forms


def home(request):
    return render(request, 'archi/index.html')


def ajout(request):
    submitted = False
    if request.method == "POST":
        form = OeuvreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Lioeuvre")
    else:
        form = OeuvreForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'archi/ajout.html',{"form": form, 'submitted':submitted})



def traitement(request):
    oform = OeuvreForm(request.POST)
    if oform.is_valid():
        oeuvre = oform.save()
        return HttpResponseRedirect(request, "/archi/")
    else:
        return render(request, "archi/ajout.html")



def update_oeuvre(request, id):
    oeuvre = Oeuvre.objects.get(pk=id)
    form = OeuvreForm(request.POST or None, instance=oeuvre)
    if form.is_valid():
        form.save()
        return redirect("Lioeuvre")
    return render(request, 'archi/update_oeuvre.html', {'oeuvre':oeuvre, 'form':form} )


def delete(request, id):
    oeuvre= models.Oeuvre.objects.get(pk=id)
    oeuvre.delete()
    return redirect("Lioeuvre")

def liste_oeuvre (request):
    liste_oeuvre = Oeuvre.objects.all()
    return render(request, 'archi/liste_oeuvre.html',{'liste_oeuvre':liste_oeuvre})


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

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        Oeuvres = Oeuvre.objects.filter(nom__contains=searched)

        return render(request, 'archi/search.html', {'searched': searched, 'Oeuvres': Oeuvres})
    else:
        return render(request, 'archi/search.html', {})


