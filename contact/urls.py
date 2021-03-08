from django.urls import path
from . import views

urlpatterns = [
    path("", views.employeeList, name="employee"),
    path("detail/<str:pk>/", views.employeeDetail, name="detail"),
    path("create", views.employeeCreate, name="create"),
    path("update/<str:pk>", views.employeeEdit, name="update"),
    path("delete/<str:pk>/", views.employeeDelete, name="delete"),
]
