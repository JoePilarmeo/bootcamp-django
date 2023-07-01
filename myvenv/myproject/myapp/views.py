from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.db.models import Q
from django.contrib import messages

from myproject.myapp.models import Student, Course, College
from myproject.myapp.forms import StudentForm, CourseForm, CollegeForm

class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-created_at")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("-created_at").filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | 
            Q(email_address__icontains=query) | Q(year_level__icontains=query)| Q(course__course_name__icontains=query) 
            | Q(college__college_name__icontains=query))
        return qs
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    context_object_name = 'student'
    template_name = 'student-update.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
      messages.success(self.request, "Student was updated successfully!")
      super().form_valid(form)
      return HttpResponseRedirect(self.get_success_url())  

class CourseList(ListView):
    model = Course
    context_object_name = 'course'
    template_name = 'course-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(CourseList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-created_at")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("-created_at").filter(Q(course_name__icontains=query))
        return qs
    
class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    context_object_name = 'course'
    template_name = 'course-update.html'
    success_url = "/course-list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
      messages.success(self.request, "Course was updated successfully!")
      super().form_valid(form)
      return HttpResponseRedirect(self.get_success_url())
    

class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-created_at")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("-created_at").filter(Q(college_name__icontains=query))
        return qs
    
class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    context_object_name = 'college'
    template_name = 'college-update.html'
    success_url = "/college-list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
      messages.success(self.request, "College was updated successfully!")
      super().form_valid(form)
      return HttpResponseRedirect(self.get_success_url())



# ADD FUNCTIONS
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'New student added successfully!')
            return redirect('StudentAdd')

        else:
            messages.error(request, 'Please complete the required field.')
            return redirect('StudentAdd')
    else:
        form = StudentForm()
        return render(request, 'student-add.html',  {'form': form})
    

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'New course added successfully!')
            return redirect('CourseAdd')

        else:
            messages.error(request, 'Please complete the required field.')
            return redirect('CourseAdd')
    else:
        form = CourseForm()
        return render(request, 'course-add.html',  {'form': form})


def add_college(request):
    if request.method == "POST":
        form = CollegeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'New college added successfully!')
            return redirect('CollegeAdd')

        else:
            messages.error(request, 'Please complete the required field.')
            return redirect('CollegeAdd')
    else:
        form = CollegeForm()
        return render(request, 'college-add.html',  {'form': form})


# DELETE FUNCTIONS
def delete_student(request, id):
  student = Student.objects.get(id=id)
  student.delete()
  messages.success(request, 'Student deleted successfully!')
  return HttpResponseRedirect(reverse('StudentList'))

def delete_course(request, id):
  course = Course.objects.get(id=id)
  course.delete()
  messages.success(request, 'Course deleted successfully!')
  return HttpResponseRedirect(reverse('CourseList'))

def delete_college(request, id):
  college = College.objects.get(id=id)
  college.delete()
  messages.success(request, 'College deleted successfully!')
  return HttpResponseRedirect(reverse('CollegeList'))