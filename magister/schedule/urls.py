from .views import index_view, search_view
from django.urls import path

urlpatterns = [
    path('', index_view, name = 'index'),
    path('search/', search_view, name = 'search'),
    #path nuevos_profesores
    
]