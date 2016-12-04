from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    """Department data models."""

    name = models.CharField(max_length=100)


class Employee(User):
    """Employees data models."""

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def name(self):
        """Full name from employees."""
        return '%s %s' % (self.first_name, self.last_name)
