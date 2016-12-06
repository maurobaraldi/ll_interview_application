from model_mommy import mommy
from django.test import TestCase
from ..models import Department, Employee


class DepartmentTestMommy(TestCase):
    """Department's modle test case."""

    def test_department_creation_mommy(self):
        """Test create department's model."""
        new_department = mommy.make('employees.Department')
        self.assertTrue(isinstance(new_department, Department))
        self.assertEqual(new_department.__str__(), new_department.name)


class EmployeeTestMommy(TestCase):
    """Employee's model test cazse."""

    def test_employee_creation_mommy(self):
        """Test create department's model."""
        new_employee = mommy.make('employees.Employee')
        self.assertTrue(isinstance(new_employee, Employee))
        self.assertEqual(new_employee.__str__(), '%s %s' % (new_employee.first_name, new_employee.last_name))
