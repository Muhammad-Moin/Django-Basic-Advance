from django.shortcuts import render,HttpResponse
from .models import Employee
# Create your views here.
def index(request):

    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)
def remove_emp(request):
    return render(request,'remove_emp.html')
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role = request.POST['role']
        phone = request.POST['phone']
        hire_date = request.POST['hire_date']
        new_emp = Employee(first_name=first_name, last_name=last_name,salary=salary,bonus=bonus,dept_id=dept
                 ,phone=phone,hire_date=hire_date,role_id=role)
        new_emp.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("Error")

def filter_emp(request):
    return render(request,'filter_emp.html')


