from django.http import HttpRequest
from django.db.models import Q
from app_data.forms import Form_Ministro, Form_Partido, Form_Presidente
from app_data.models import Presidente, Ministro, Partido
from django.shortcuts import render

# Create your views here.

class Form_Presidente_View(HttpRequest):

    def register_president(request):
        presidente = Form_Presidente()
        return render(request, 'app_data/presidente.html', {'form':presidente})
    
    def check_info_president(request):
        presidente = Form_Presidente(request.POST)
        if presidente.is_valid():
            presidente.save()
            presidente = Form_Presidente()
        return render(request, 'app_data/presidente.html', {'form':presidente, 'check':'Registro exitoso'})
    
    def search_president(request):
        busqueda = request.GET.get('Buscar')
        registros = Presidente.objects.all()
        
        if busqueda:
            registros = Presidente.objects.filter(
                Q(nombre__icontains = busqueda) |
                Q(apellido__icontains = busqueda) |
                Q(asume_cargo__icontains = busqueda) |
                Q(deja_cargo__icontains = busqueda) |
                Q(partido__icontains = busqueda) |
                Q(constitucional__icontains = busqueda)).distinct()
        return render(request, 'app_data/reg_presidentes.html',{'registros':registros})



class Form_Ministro_View(HttpRequest):

    def register_minister(request):
        ministro = Form_Ministro()
        return render(request, 'app_data/ministro.html', {'form':ministro})
    
    def check_info_minister(request):
        ministro = Form_Ministro(request.POST)
        if ministro.is_valid():
            ministro.save()
            ministro = Form_Ministro()
        return render(request, 'app_data/ministro.html', {'form':ministro, 'check':'Registro existoso'})
    
    def search_ministro(request):
        busqueda = request.GET.get('Buscar')
        registros = Ministro.objects.all()
        
        if busqueda:
            registros = Ministro.objects.filter(
                Q(nombre__icontains = busqueda) |
                Q(apellido__icontains = busqueda) |
                Q(asume_cargo__icontains = busqueda) |
                Q(deja_cargo__icontains = busqueda) |
                Q(cartera__icontains = busqueda)).distinct()
        return render(request, 'app_data/reg_ministros.html',{'registros':registros})



class Form_Partido_View(HttpRequest):

    def register_party(request):
        partido = Form_Partido()
        return render(request, 'app_data/partido.html', {'form':partido})
    
    def check_info_party(request):
        partido = Form_Partido(request.POST)
        if partido.is_valid():
            partido.save()
            partido = Form_Partido()
        return render(request, 'app_data/partido.html', {'form':partido, 'check':'Registro existoso'})
    
    def search_partido(request):
        busqueda = request.GET.get('Buscar')
        registros = Partido.objects.all()
        
        if busqueda:
            registros = Partido.objects.filter(
                Q(nombre__icontains = busqueda) |
                Q(fundacion__icontains = busqueda) |
                Q(antiguedad__icontains = busqueda)).distinct()
        return render(request, 'app_data/reg_partidos.html',{'registros':registros})