from django.contrib.auth.models import Group, User
from rest_framework import serializers

from luizalabs.employees.models import Department, Employee


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Users model serializer class."""

    class Meta:
        model = User
        fields = 'url first_name email groups'.split()


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Group model serializer class."""

    class Meta:
        model = Group
        fields = ('url', 'first_name')


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee model serializer class."""

    name = serializers.SerializerMethodField('get_employee_name')
    department = serializers.SerializerMethodField('get_employee_department')

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')

    def get_employee_name(self, obj):
        return '%s %s' % (obj.first_name, obj.last_name)

    def get_employee_department(self, obj):
        return obj.department.name


class DepartmentSerializer(serializers.ModelSerializer):
    """Department model serializer class."""

    class Meta:
        model = Department
        fields = ('name', )
