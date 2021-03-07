from django.shortcuts import render
from django.http import HttpResponse
from demoproject.models import sqlserverconnection
from demoproject.models import Insertdata, Insertname
import pyodbc
import json as simplejson

connection = pyodbc.connect('Driver={sql server};'
                            'Server=DESKTOP-OF8D1IH;'
                            'Database=DjangoDatabase;'
                            'Trusted_Connection=yes;')


def HomePage(request):
    return render(request, 'HomePage.html')


def InsertRecord(request):
    cursor = connection.cursor()

    if request.method == 'POST':
        if request.POST.get('Empname') and request.POST.get('EmpEmail') and request.POST.get('EmpSalary'):
            insertstvalues = Insertdata()
            insertstvalues.Empname = request.POST.get('Empname')
            insertstvalues.Email = request.POST.get('EmpEmail')
            insertstvalues.Salary = request.POST.get('EmpSalary')

            cursor.execute("insert into EmployeeRecord values ('"+insertstvalues.Empname +
                           "','"+insertstvalues.Email+"','"+insertstvalues.Salary+"')")
            cursor.commit()
            return render(request, 'Insert.html')
    else:
        return render(request, 'Insert.html')
    return render(request, 'Insert.html')


def UpdateRecord(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        if request.POST.get('Empname'):
            insertdata = Insertname()
            insertdata.Empname = request.POST.get('Empname')
            cursor.execute(
                "select * from EmployeeRecord where Empname='"+insertdata.Empname+"'")
            result = cursor.fetchall()
            print(result)
            return render(request, 'Update.html', {'sqlserverconnection': result})
        elif request.POST.get('UpEmpname') and request.POST.get('UpEmpEmail') and request.POST.get('UpEmpSalary'):
            insertstvalues = Insertdata()
            insertstvalues.Empname = request.POST.get('UpEmpname')
            insertstvalues.Email = request.POST.get('UpEmpEmail')
            insertstvalues.Salary = request.POST.get('UpEmpSalary')

            cursor.execute("UPDATE EmployeeRecord SET Email='"+insertstvalues.Email +
                           "',Salary="+insertstvalues.Salary+" Where Empname='"+insertstvalues.Empname+"';")
            cursor.commit()

            cursor.execute(
                "select * from EmployeeRecord where Empname='"+insertstvalues.Empname+"'")
            result = cursor.fetchall()
            return render(request, 'Update.html', {'sqlserverconnection': result})

        return render(request, 'Update.html')
    else:
        return render(request, 'Update.html')


def DisplayRecord(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        if request.POST.get('fname'):
            insertdata = Insertname()
            insertdata.Empname = request.POST.get('fname')

            cursor.execute(
                "select * from EmployeeRecord where Empname='"+insertdata.Empname+"'")
            result = cursor.fetchall()
            return render(request, 'Display.html', {'sqlserverconnection': result})

        elif request.POST.get('button_name') == 'all_Record':
            cursor.execute("select * from EmployeeRecord")
            result = cursor.fetchall()
            return render(request, 'Display.html', {'sqlserverconnection': result})

        else:
            return render(request, 'Display.html')

    else:
        return render(request, 'Display.html')


def DeleteRecord(request):
    return render(request, 'Delete.html')
