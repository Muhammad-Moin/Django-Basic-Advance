from django.contrib import admin
from .models import Department,Role,Employee
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','dept','role')
    search_fields = ('first_name',)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Employee,EmployeeAdmin)

