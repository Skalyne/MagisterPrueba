from .models import Schedule
from .quickstart import get_sheet, read_horarios, read_profesores



def actualizar_horarios():
    data_sheet = read_horarios(get_sheet())    
    for item in data_sheet:
        obj = Schedule(id = item[0],
        fecha = datetime.strptime(item[1], '%d/%m/%Y').strftime("%Y-%m-%d"),
        dia = item[2],
        h_inicio= item[3],
        h_fin= item[4],
        grupo= item[5],
        profe= item[6]
        )
        obj.save()

        
        print(item)
        
def actualizar_profesores():
    data_sheet = read_profesores(get_sheet())    
    for item in data_sheet:
        obj = Schedule(DNI = item[0],
        nombre = item[1],
        apellido = item[2],
        movil = item[3]
        )
        obj.save()
