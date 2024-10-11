from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('students', views.index,name='index'),
    path('insert',views.insertdata,name='insert'),
    path('update/<id>',views.updateData,name='update'),
    path('delete/<id>',views.deleteData,name='delete')
]
