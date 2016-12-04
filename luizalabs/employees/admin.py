from django.contrib import admin

from luizalabs.employees.models import Department, Employee

admin.site.register(Employee)
admin.site.register(Department)
