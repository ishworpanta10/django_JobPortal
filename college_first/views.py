from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.contrib import messages

from company.models import Company

from employee.models import Employee

# for checking username and password
from django.contrib.auth import authenticate, login, logout


def who(request):
    return render(request, 'who.html')


def test(request):
    return render(request, 'test.html')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        # post request is mentioned in form
        # or user = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        user_name = request.POST['username']
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            user = User(username=user_name, first_name=first_name,
                        last_name=last_name, email=email)
            user.set_password(pass1)
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your account is created')
            return redirect('login')

        else:
            messages.add_message(request, messages.ERROR,
                                 'Password does not match')
            return redirect('signup')


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # usernaem is name field of password tag in form
        user_name = request.POST.get('username')
        # pass is name field of password tag in form
        password = request.POST.get('pass')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            w = whoareyou(request.user.id)  # taking current user
            if w == 1:
                return redirect('employee_dashboard')
            elif w == 2:
                return redirect('company_dashboard')
            else:
                return redirect('who')

        else:
            messages.add_message(request, messages.ERROR,
                                 'Username or Password do not match')
            return redirect('login')

# old way using if else condn:
            # def dashboard(request):
            #     if request.user.is_authenticated:
            #         return render(request, 'dashboard.html')
            #     else:
            #         return redirect('login')

            # new way


@login_required(login_url="login")
def dashboard(request):
    return render(request, 'company_dashboard.html')


def signout(request):
    logout(request)
    return redirect('login')


# to find if current user is employee or comany or new user
def whoareyou(id):
    try:
        a = Employee.objects.get(user_id=id)
        return 1
    except:
        try:
            c = Company.objects.get(user_id=id)
            return 2

        except:
            return 0
