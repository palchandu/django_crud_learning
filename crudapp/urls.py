from django.contrib import admin
from django.urls import path
from crudapp import views
urlpatterns = [
   path("",views.index,name='Crud')
]
