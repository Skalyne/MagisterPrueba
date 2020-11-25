from django.shortcuts import render
from .models import Schedule, Profesores
from datetime import datetime
from .quickstart import get_sheet, read_horarios, read_profesores,write_to_spreadsheet
from django.views.generic import CreateView
from .forms import Profesform
from django.http import HttpResponseRedirect





def actualizar_horarios():
    data_sheet = read_horarios(get_sheet())    
    for item in data_sheet:
        
        obj = Schedule(id = item[0],
        fecha = datetime.strptime(item[1], '%d/%m/%Y').strftime("%Y-%m-%d"),
        dia = item[2],
        h_inicio= item[3],
        h_fin= item[4],
        grupo= item[5],
        profe= Profesores.objects.get(DNI = item[6].replace("'",""))
        )
        obj.save()

        
        print(item)
        
def actualizar_profesores():
    data_sheet = read_profesores(get_sheet())    
    for item in data_sheet:
        
        obj = Profesores(DNI = item[0],
        nombre = item[1],
        apellido = item[2]
        )
        try:
            obj.movil = item[3]
            obj.save()
        except:
            obj.save()






# Create your views here.

        
def get_name(request):
    if request.method == 'POST':        
        form = Profesform(request.POST)
        
        write_to_spreadsheet(get_sheet(),request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = Profesform()
    return render(request, 'add_profe.html', {'form': form})


def index_view(request):

    actualizar_horarios()
    context = {}
    clases = Schedule.objects.all()

    profe_list = Schedule.objects.values('profe').distinct()
    grupos_list = Schedule.objects.values('grupo').distinct()

    context = {
        "all_classes": clases,
        'profe_list': profe_list,
        'grupos_list': grupos_list
    }

    return render(request, 'index.html', context)


def search_view(request):   

    profe_list = Schedule.objects.values('profe').distinct()
    grupos_list = Schedule.objects.values('grupo').distinct()
    clases_searched = Schedule.objects.all()
    
    
    context = {
        'profe_list': profe_list,
        'grupos_list': grupos_list,
        'clases_searched':clases_searched,
    }

    context = {}
    filters={}

    if request.POST:
        data = request.POST
        if data['class_date'] != '':
            filters['fecha'] = datetime.strptime(data['class_date'], '%Y-%m-%d')

        if (data['profe_selection'] != 'Todos los profesores'):    
            filters['profe'] = data['profe_selection']  
                  
        if data['grupo_selection'] != 'Todos los Grupos':
            filters['grupo'] = data['grupo_selection']



            #datetime.strptime(data['class_date'], '%Y-%m-%d').strftime("%d/%m/%Y")
        print(data)

    context['clases_searched'] = Schedule.objects.filter(**filters)


    return render(request, 'search.html', context)