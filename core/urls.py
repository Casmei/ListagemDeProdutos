#Importando o Path que irá conectar a Url
from django.urls import path
#Importando as Views
from .views import index, contato, produto

urlpatterns = [
    path("", index, name='index'),
    path("contato", contato),
    path('produto/<int:pk>', produto, name='produto'),
]
