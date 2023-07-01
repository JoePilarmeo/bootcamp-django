from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Course(BaseModel):
    course_name = models.CharField(max_length=500)
    
    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.course_name}"
    

class College(BaseModel):
    college_name = models.CharField(max_length=500)
    
    class Meta:
        verbose_name_plural = "Colleges"

    def __str__(self):
        return f"{self.college_name}"


class Student(BaseModel):
    YEAR_LEVEL_CHOICES = (('1st Year','1st Year'), ('2nd Year','2nd Year'), ('3rd Year','3rd Year'), ('4th Year', '4th Year'))
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email_address = models.CharField(max_length=300)
    year_level = models.CharField(max_length=20, choices=YEAR_LEVEL_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"