from django.shortcuts import render
from django.http import HttpResponse
from demoproject.models import sqlserverconnection
from demoproject.models import Insertdata
import pyodbc

def HomePage(request):
    return render(request,'HomePage.html')

def InsertRecord(request):
    return render(request,'Insert.html')

def UpdateRecord(request):
    return render(request, 'Update.html')

def SearchRecord(request):
    return render(request, 'Display.html')

def DeleteRecord(request):
    return render(request, 'Delete.html') 

def connectionsql(request):
    connection=pyodbc.connect('Driver={sql server};'
                                'Server=DESKTOP-OF8D1IH;'
                                'Database=DjangoDatabase;'
                                'Trusted_Connection=yes;')

    cursor=connection.cursor()
    cursor.execute("select * from EmployeeRecord")
    result = cursor.fetchall()
    return render(request,'index.html',{'sqlserverconnection':result})


def saverecords(request):
    connection = pyodbc.connect('Driver={sql server};'
                                'Server=DESKTOP-OF8D1IH;'
                                'Database=DjangoDatabase;'
                                'Trusted_Connection=yes;')

    cursor=connection.cursor()

    if request.method == 'POST':
        if request.POST.get('Empname') and request.POST.get('EmpEmail') and request.POST.get('EmpSalary'):
            insertstvalues = Insertdata()
            insertstvalues.Empname = request.POST.get('Empname')
            insertstvalues.Email = request.POST.get('EmpEmail')
            insertstvalues.Salary = request.POST.get('EmpSalary')

            cursor.execute("insert into EmployeeRecord values ('"+insertstvalues.Empname+"','"+insertstvalues.Email+"','"+insertstvalues.Salary+"')")
            cursor.commit()
            return render(request,'Insert.html')
    else:
        return render(request,'Insert.html')
