from django.contrib import admin
from django.urls import path

from myapp.views import StudentList, CourseList, CollegeList, StudentUpdateView, CourseUpdateView, CollegeUpdateView
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.StudentList.as_view(), name='StudentList'),
    path('student-list/add', views.add_student, name='StudentAdd'),
    path('student-list/<pk>', StudentUpdateView.as_view(), name="StudentUpdate"),
    path('delete_student/<int:id>', views.delete_student, name='StudentDelete'),

    path('course-list', CourseList.as_view(), name='CourseList'),
    path('course-list/add', views.add_course, name='CourseAdd'),
    path('course-list/<pk>', CourseUpdateView.as_view(), name="CourseUpdate"),
    path('delete_course/<int:id>', views.delete_course, name='CourseDelete'),

    path('college-list', CollegeList.as_view(), name='CollegeList'),
    path('college-list/add', views.add_college, name='CollegeAdd'),
    path('college-list/<pk>', CollegeUpdateView.as_view(), name="CollegeUpdate"),
    path('delete_college/<int:id>', views.delete_college, name='CollegeDelete'),

]