from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='employee_dashboard'),
    path('create_employee/', views.createEmployee, name='create_employee')

]
