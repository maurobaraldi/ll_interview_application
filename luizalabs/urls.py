"""luizalabs URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from luizalabs.employees import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'departments', views.DepartmentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
