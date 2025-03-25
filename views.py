from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context= {
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        phone = int(request.POST.get('phone'))
        dept = int(request.POST.get('dept'))
        role = int(request.POST.get('role'))

        if not (first_name and last_name and salary and bonus and phone and dept and role):
            return HttpResponse("All fields are required!")

        # try:
        #     salary = int(salary)
        #     bonus = int(bonus)
        #     phone = int(phone)
        #     dept = Department.objects.get(id=int(dept_id))
        #     role = Role.objects.get(id=int(role_id))
        # except (ValueError, Department.DoesNotExist, Role.DoesNotExist):
        #     return HttpResponse("Invalid input data!")

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            dept_id=dept,
            role_id=role,
            hire_date=datetime.now()
        )
        new_emp.save()
        return HttpResponse('Employee added Successfully')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')

    return HttpResponse("An Exception Occurred! Employee Has Not Been Added")

    #  if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     salary = int(request.POST['salary'])
    #     bonus = int(request.POST['bonus'])
    #     phone = int(request.POST['phone'])
    #     dept = int(request.POST['dept'])
    #     role = int(request.POST['role'])
    #     new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
    #     new_emp.save()
    #     return HttpResponse('Employee added Successfully')
    # elif request.method =='GET':
    #     return render(request, 'add_emp.html')
    # else:
    #     return HttpResponse("An Exception Occured! Employee Has Not Been Added")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(emps)
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
