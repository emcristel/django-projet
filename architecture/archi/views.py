from django.shortcuts import render
from .forms import TableForm
from . import models
from django.http import HttpResponseRedirect
from django import forms


def index(request):
    submitted = False
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = TableForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "ajout.html", {'ajout': form})


def ajout(request):
    if request.method=="POST":
        form = TableForm(request)
        if form.is_valid():
            archi = form.save()
            return HttpResponseRedirect(request,'/archi/affiche/')
        else:
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

def affiche(request, id):
    oeuvre = models.Table.objects.get(pk=id)
    return render(request,"archi/affiche.html",{"form": form})

def update(request, id):
    oeuvre=models.Table.objects.get(pk=id)
    oform= TableForm(oeuvre.form)
    return render(request,"archi/update.html", {"form": oform,"id": id})

def traitementupdate(request, id):
    oform = OTableForm(request.POST)
    if oform.is_valid():
        oeuvre = oform.save(commit=False)
        oeuvre.id = id;
        oeuvre.save()
        return HttpResponseRedirect("/archi/")
    else:
        return render(request, "archie/update.html", {"form": oform, "id": id})


def delete(request, id):
    oeuvre= models.Table.objects.get(pk=id)
    oeuvre.delete()
    return HttpResponseRedirect("/archi/")

def tous (request):
    oeuvre= list(models.Table.objects.all())
    return render(request, 'tous.html',{'oeuvre':oeuvre})


#def ajout_architecte(request):
 #   submitted = False
  #  if request.method == 'POST':
  #      form = ArchitecteForm(request.POST)
  #      if form.is_valid():
  #          form.save()
  #          return redirect('liste_architecte')
  #  else:
  #      form = ArchitecteForm
  #      if 'submitted' in request.GET:
  #          submitted = True
  #  return render(request, 'archi/ajout_architecte.html', {'form':form, 'submitted':submitted})

#def all_architecte(request):
 #   liste_architecte = Architecte.objects.all()
  #  return render(request, 'archi/liste_architecte.html', {'liste_architecte': liste_architecte})

#def update_architecte(request, architecte_id):
 #   architecte = Architecte.objects.get(pk=ville_id)
  #  form = ArchitecteForm(request.POST or None, instance=architecte)
   # if form.is_valid():
    #    form.save()
     #   return redirect("liste_architecte")
    #return render(request, 'archi/update_architecte.html', {'architecte':architecte, 'form':form} )

#def delete_architecte(request, architecte_id):
 #   architecte = Architecte.objects.get(pk=ville_id)
  #  architecte.delete()
    # return redirect('liste_architecte')