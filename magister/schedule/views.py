from django.shortcuts import render
from .models import Schedule
from .quickstart import main as get_sheet_data

from datetime import datetime
# Create your views here.
def compare():
    objint = Schedule.objects.all()    
    objlist = []
    for item in objint:
        objlist = [item.id,item.fecha,item.dia,item.h_inicio,item.h_fin,item.grupo,item.profe]
        print(objlist)

def actualizar():
    data_sheet = get_sheet_data()    
    for item in data_sheet:
        obj = Schedule(id = item[0],
        fecha = datetime.strptime(item[1], '%d/%m/%Y').strftime("%Y-%m-%d"),
        dia = item[2],
        h_inicio= item[3],
        h_fin= item[4],
        grupo= item[5],
        profe= item[6]
        )

        
        print(item)
        


        



def index_view(request):
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
    actualizar()
    compare()
    profe_list = Schedule.objects.values('profe').distinct()
    grupos_list = Schedule.objects.values('grupo').distinct()
    clases_searched = Schedule.objects.all()
    context = {}
    filters={}
    context = {
        'profe_list': profe_list,
        'grupos_list': grupos_list,
        'clases_searched':clases_searched,
    }

    if request.POST:

        data = request.POST
        if (data['profe_selection'] != ['Todos los profesores']):    
            filters['profe'] = data['profe_selection']  
                  
        if data['grupo_selection'] != 'Todos los Grupos':
            filters['grupo'] = data['grupo_selection']

        if data['class_date'] != '':
            pass

    context['clases_searched'] = Schedule.objects.filter(**filters)


    return render(request, 'search.html', context)