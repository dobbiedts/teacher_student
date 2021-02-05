from django.db import models
import uuid

# Create your models here.



# Create your models here.
class student(models.Model):
    stud_no = models.CharField(max_length = 10, help_text = "Enter student number", default = None)
    first_name = models.CharField(max_length = 20, help_text = "Enter first name", default = None)
    last_name = models.CharField(max_length = 20, help_text = "Enter last name")
    class_no = models.CharField(max_length = 10, help_text = "Enter class number")
    
    class Meta:
       
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
    class Admin:
        pass
    
    
class teacher(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4, help_text ='Unique id for this teacher', editable = False )
    staff_no = models.CharField(max_length = 10, help_text = "Enter staff number" )
    full_name = models.CharField(max_length = 30, help_text = "Enter teacher full name", default = None)
    level = models.CharField(max_length = 10, help_text = "Enter teacher level")
    class_held = models.CharField(max_length = 10, help_text = "Enter class number",  blank = True)
    
    def __str__(self):
        
        return self.full_name
    
class teacher_student(teacher):
    assigned_student = models.ManyToManyField(student, help_text = 'who is/are the students assigned to this teacher', default = None)
    
    
    
    def __str__(self):
         
        return self.staff_no
        return self.full_name
        return self.assigned_student
        return self.stud_no
        return self.class_held
        return self.first_name
        return self.last_name
        return self.class_no
    
    
        
        
    def get_absolute_url(self):
        """Returns the url to access a detail record for this teacher."""
        return reverse('teacher-detail', args=[str(self.id)])
    
    def display_assigned_student(self):
        """Create a string for the student. This is required to display student in Admin."""
        return ', '.join(assigned_student.first_name for assigned_student in self.assigned_student.all()[:3])
    
    display_assigned_student.short_description = 'assigned_student'
