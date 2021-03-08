from contact.serializers import EmployeeSerializer
from contact.models import Employee
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET"])
def employeeList(request):
    employee = Employee.objects.all()
    Serializer = EmployeeSerializer(employee, many=True)
    return Response(Serializer.data)


@api_view(["GET"])
def employeeDetail(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def employeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def employeeEdit(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=employee, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def employeeDelete(request, pk):
    employee = Employee.objects.get(name=pk)
    employee.delete()
    return Response("Deleted")
