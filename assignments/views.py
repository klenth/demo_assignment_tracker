from django.shortcuts import render, get_object_or_404

from .models import *
# Create your views here.


def home(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'home.html', context)


def view_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    assignments = course.assignment_set.order_by('due_date')

    context = {
        'course': course,
        'completed_assignments': assignments.filter(complete=True),
        'uncompleted_assignments': assignments.filter(complete=False),
    }

    return render(request, 'view_course.html', context)
