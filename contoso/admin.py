from django.contrib import admin
from .models import student,teacher, teacher_student

# Register your models here.
admin.site.register(student)
admin.site.register(teacher)



class teacher_student_admin(admin.ModelAdmin):
    list_display = ('full_name', 'class_held', 'staff_no', 'display_assigned_student')
                    
    pass
admin.site.register(teacher_student, teacher_student_admin)
