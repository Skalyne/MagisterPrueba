from .views import index_view, search_view, get_name
from django.urls import path

urlpatterns = [
    path('', index_view, name = 'index'),
    path('search/', search_view, name = 'search'),
    path('add-teacher/', get_name, name= 'add_profe'),
    #path nuevos_profesores
    
]
