from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from luizalabs.employees.models import Employee, Department
from luizalabs.employees.serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    GroupSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """Users API endpoint."""

    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class GroupViewSet(viewsets.ModelViewSet):
    """"Groups API endpoints."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EmployeeViewSet(viewsets.ModelViewSet):
    """"Groups API endpoints."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class DepartmentViewSet(viewsets.ModelViewSet):
    """"Groups API endpoints."""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_serializer_context(self):
        return {'request': self.request}
