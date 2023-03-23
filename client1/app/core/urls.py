from .views import home, salvar, editar, update, deletar
from django.urls import path

urlpatterns = [
    path('', home),
    path('salvar/', salvar , name='salvar'),
    path('editar/<int:id>', editar ,name='editar'),
    path('update/<int:id>', update ,name='update'),
    path('deletar/<int:id>', deletar ,name='deletar')
]
