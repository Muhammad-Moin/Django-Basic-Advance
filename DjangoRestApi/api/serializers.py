from rest_framework import serializers
from .models import Company,Employee

class CompanySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class EmployeeSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'