from django.views.generic import View
from django.shortcuts import render

from FamiliaresApp.models import Familiares


# Create your views here.

class HomeView(View):
    def get(self, request, *args, ):
        context={

        }
        return render(request, "index.html", context)
        

def familiares(request):
    familiar1=Familiares.objects.create(
        Nombre="Ariel", 
        Apellido="Botello" , 
        Edad= 60, 
        FechaNacimiento= "17/10/1961",
        )
    familiar2=Familiares.objects.create(
        Nombre="Lucía", 
        Apellido="Fernandez" , 
        Edad= 56, 
        FechaNacimiento= "15/02/1966",
        )
    familiar3=Familiares.objects.create(
        Nombre="Victoria", 
        Apellido="Botello" , 
        Edad= 20 , 
        FechaNacimiento= "12/04/2002",
        )

    context = {"familiar_uno":familiar1, "familiar_dos":familiar2, "familiar_tres":familiar3}
    return render(request, "integrantes.html", context=context)