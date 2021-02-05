from rest_framework import serializers

from .models import student, teacher, teacher_student


class studentSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
            model= student
            fields = '__all__'
    
class teacherSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
            model = teacher
            fields = '__all__'
        
class teacher_studentSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
            model = teacher_student
            fields = '__all__'