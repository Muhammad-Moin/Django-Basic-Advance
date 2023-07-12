from django.contrib import admin
from .models import Company, Employee


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name', 'type', 'location')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address')
    list_filter = ('name', 'email')

    search_fields = ('name', 'email')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
