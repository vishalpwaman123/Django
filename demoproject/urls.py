
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('Insert/', views.InsertRecord, name='insert'),
    path('Update/', views.UpdateRecord, name='update'),
    path('Display/', views.DisplayRecord, name='display'),
    path('Delete/', views.DeleteRecord, name='delete'),
    
]
