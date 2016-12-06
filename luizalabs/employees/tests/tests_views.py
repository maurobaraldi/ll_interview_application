from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Department, Employee


class ReadUserTest(APITestCase):
    """Users API test case."""

    def setUp(self):
        """Setup test class."""
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="Mike", email="mike@mikemail.com")

    def test_can_read_user_list(self):
        """Test retrieve list of users."""
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 2)

    def test_can_read_user_detail(self):
        """Test retrieve details from user."""
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'mike@mikemail.com')


class ReadDepartmentTest(APITestCase):
    """Departments API test case."""

    def setUp(self):
        """Setup test class."""
        self.department = Department.objects.bulk_create([
            Department(name='Enginering'),
            Department(name='Architecture'),
            Department(name='Managment')
        ])

    def test_can_read_department_list(self):
        """Test retrieve list of departments."""
        response = self.client.get(reverse('department-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 3)


class ReadEmployeeTest(APITestCase):
    """Employees API test case."""

    def setUp(self):
        """Setup test class."""
        Employee.objects.create(**{
            'username': 'johnsnow',
            'first_name': 'John',
            'last_name': 'Snow',
            'email': 'johnsnow@thewall.com',
            'department': Department.objects.create(name='Architecture')
        })
        Employee.objects.create(**{
            'username': 'hodor',
            'first_name': 'Hold',
            'last_name': 'Door',
            'email': 'hodor@winterfell.com',
            'department': Department.objects.create(name='Enginering')
        })

    def test_can_read_department_list(self):
        """Test retrieve details from user."""
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 2)
