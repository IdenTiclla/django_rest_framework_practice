from django.shortcuts import render
import rest_framework
from rest_framework import response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from drfapp.serializers import StudentSerializer

from drfapp.models import Student

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        student1 = qs.first()
        serializer = StudentSerializer(student1)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)