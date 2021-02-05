from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView

from .serializers import studentSerializer, teacherSerializer, teacher_studentSerializer

from .models import student, teacher, teacher_student



# Create your views here.

class studentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    
class studentSubClassFieldsMixin(object):

    def get_queryset(self):
        return student.objects.select_subclasses()
    
class RetrievestudentAPIView(studentSubClassFieldsMixin, generics.RetrieveDestroyAPIView):
    serializer_class = studentSerializer 
    
class teacherViewSet(viewsets.ModelViewSet):
    queryset = teacher.objects.all().order_by('full_name')
    serializer_class = teacherSerializer

class teacherSubClassFieldsMixin(object):

    def get_queryset(self):
        return teacher.objects.select_subclasses()
    
class RetrieveteacherAPIView(teacherSubClassFieldsMixin, generics.RetrieveDestroyAPIView):
    serializer_class = teacherSerializer 
    
class teacher_studentViewSet(viewsets.ModelViewSet):
    queryset = teacher_student.objects.all().order_by('full_name')
    serializer_class = teacher_studentSerializer

    
    
    