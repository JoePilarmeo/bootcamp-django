from django.contrib import admin

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email_address", "year_level", "course", "college")
    search_fields =("first_name","last_name","email_address", "year_level", "course", "college")
    list_filter = ("created_at",)


from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=("course_name",)
    search_fields =("course_name",)
    list_filter = ("created_at",)


from .models import College

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display=("college_name",)
    search_fields =("college_name",)
    list_filter = ("created_at",)