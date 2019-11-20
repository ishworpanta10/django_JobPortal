from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_no = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    qualification = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        # fields = '__all__' # for all fields
        # fields = ['fullname', 'contact_no'] # for only neede
        exclude = ['user']
