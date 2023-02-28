from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee

# Create your templates here.
# .save() is the ORM equivalent of the SQL insert to statement.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})

# .all() is the ORM equivalent of the SQL statement "SELECT * FROM tablename"
def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})


# .get is the ORM equivalent of the SQL statement "SELECT * FROM tablename WHERE id = ? "
# method update carries the update process for a single record
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})

# .delete() is the ORM equivalent of the statement SQL : " DELETE FROM tablename WHERE id = ? "
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")



























