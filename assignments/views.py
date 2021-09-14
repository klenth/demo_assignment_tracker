from django.shortcuts import render, get_object_or_404, redirect

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


def easter_egg(request):
    context = {

    }

    return render(request, 'easter_egg.html', context)


def parameters(request):
    context = {

    }
    return render(request, 'parameters.html', context)


def new_course(request):
    context = {
        'errors': [],
    }

    if request.method == 'POST':
        # The form is being submitted
        # request.POST is a dictionary of all the form values
        new_title = request.POST.get('new_title') # returns None if there is no new_title

        # Validate the input
        if new_title is None or new_title.strip() == '':
            context['errors'].append('Must specify a title')
        elif len(new_title) > 64:
            context['errors'].append('Title too long (must be 64 characters or fewer)')

        if not context['errors']:
            # context['errors'] is empty, so all validation steps passed
            new_course = Course(title=new_title)
            new_course.save()

            return redirect('home') # Redirect to home page

    return render(request, 'edit_course.html', context)






