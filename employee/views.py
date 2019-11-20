from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required

from .form import EmployeeForm

# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'employee_dashboard.html')


def createEmployee(request):
    if request.method == 'GET':
        context = {
            'form': EmployeeForm()
        }
        return render(request, 'create_employee.html', context)

    else:
        form = EmployeeForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user_id
            data.save()
            return redirect('employee_dashboard')
        else:
            return redirect('create_employee')
