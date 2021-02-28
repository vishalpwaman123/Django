from django.shortcuts import render
from django.http import HttpResponse
from demoproject.models import sqlserverconnection
import pyodbc

def connectionsql(request):
    connection=pyodbc.connect('Driver={sql server};'
                                'Server=DESKTOP-OF8D1IH;'
                                'Database=DjangoDatabase;'
                                'Trusted_Connection=yes;')

    cursor=connection.cursor()
    cursor.execute("select * from EmployeeRecord")
    result = cursor.fetchall()
    return render(request,'index.html',{'sqlserverconnection':result})