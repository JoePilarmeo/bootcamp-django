from django.forms import ModelForm
from .models import Student, Course, College

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "email_address", "year_level", "course", "college",)

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ("course_name",)

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = ("college_name",)