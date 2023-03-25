from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict
from AppEdukate.models import Course, Student, Teacher, Assignment
from AppEdukate.forms import Form_courses, Form_students, Form_teachers, Form_assignment
from django.contrib.auth.decorators import login_required



##########################################
#                 MENU                   #
##########################################

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "AppEdukate/about.html")


def detail(request):
    return render(request, "AppEdukate/detail.html")


def feature(request):
    return render(request, "AppEdukate/feature.html")


def team(request):
    return render(request, "AppEdukate/team.html")


def testimonial(request):
    return render(request, "AppEdukate/testimonial.html")


def contact(request):
    return render(request, "AppEdukate/contact.html")


##########################################
#                SEARCH                  #
##########################################

@login_required
def search_courses(request):
    return render(request, "AppEdukate/search_courses.html")


def courses(request):
    name = request.GET.get('name')
    commission = request.GET.get('commission')
    min_length = 3
    if not name and not commission:
        answer = "You did not enter data"
        return HttpResponse(answer)
    if name and len(name) < min_length:
        answer = f"Enter at least {min_length} characters"
        return HttpResponse(answer)
    courses = Course.objects.all()
    if name:
        courses = courses.filter(name__icontains=name)
    if commission:
        courses = courses.filter(commission=commission)
    if courses.exists():
        return render(request, "AppEdukate/results_search_courses.html", {'courses': courses, 'commission': commission})
    else:
        answer = "No results found"
        return HttpResponse(answer)


@login_required
def search_students(request):
    return render(request, "AppEdukate/search_students.html")


def students(request):
    name = request.GET.get('name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    min_length = 3
    if not name and not last_name and not email:
        answer = "You did not enter data"
        return HttpResponse(answer)
    if name and len(name) < min_length:
        answer = f"Enter at least {min_length} characters"
        return HttpResponse(answer)
    if last_name and len(last_name) < min_length:
        answer = f"Enter at least {min_length} characters"
        return HttpResponse(answer)
    if email and len(email) < min_length:
        answer = f"Enter at least {min_length} characters"
        return HttpResponse(answer)
    students = Student.objects.all()
    if name:
        name = name.lower()
        students = students.filter(name__icontains=name)
    if last_name:
        last_name = last_name.lower()
        students = students.filter(last_name__icontains=last_name)
    if email:
        email = email.lower()
        students = students.filter(email__icontains=email)
    if students.exists():
        return render(request, "AppEdukate/results_search_students.html", {'students': students, 'last_name': last_name,
                                                                           'email': email})
    else:
        answer = "No results found"
        return HttpResponse(answer)


@login_required
def search_teachers(request):
    return render(request, "AppEdukate/search_teachers.html")


def teachers(request):
    name = request.GET.get('name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    profession = request.GET.get('profession')
    min_length = 3
    if not name and not last_name and not email and not profession:
        answer = "You did not enter data"
        return HttpResponse(answer)
    if name and len(name) < min_length:
        answer = f"Enter at least {min_length} characters"
        return HttpResponse(answer)
    if last_name and len(last_name) < min_length:
        answer = f"Enter at least {min_length} characters"
        return HttpResponse(answer)
    if email and len(email) < min_length:
        answer = f"Enter at least {min_length} characters"
        return HttpResponse(answer)
    if profession and len(profession) < min_length:
        answer = f"Enter at least {min_length} characters"
        return HttpResponse(answer)
    teachers = Teacher.objects.all()
    if name:
        name = name.lower()
        teachers = teachers.filter(name__icontains=name)
    if last_name:
        last_name = last_name.lower()
        teachers = teachers.filter(last_name__icontains=last_name)
    if email:
        email = email.lower()
        teachers = teachers.filter(email__icontains=email)
    if profession:
        profession = profession.lower()
        teachers = teachers.filter(profession__icontains=profession)
    if teachers.exists():
        return render(request, "AppEdukate/results_search_teachers.html", {'teachers': teachers, 'last_name': last_name,
                                                                           'email': email, 'profession': profession})
    else:
        answer = "No results found"
        return HttpResponse(answer)


##########################################
#                 FORMS                  #
##########################################


@login_required
def form_courses(request):
    if request.method == 'POST':
        min_length = 3
        my_form = Form_courses(request.POST)
        if my_form.is_valid() and len(my_form.cleaned_data['course']) >= min_length:
            information = my_form.cleaned_data
            course = Course(name=information['course'].lower(),
                            commission=int(information['commission']))
            course.save()
            success_message = "Course Created"
            return render(request, "AppEdukate/redirect_forms.html", {"success_message": success_message})
        else:
            my_form.add_error('course', f'The course name must have more than {min_length} characters')
    else:
        my_form = Form_courses()
    return render(request, "AppEdukate/form_courses.html", {"my_form": my_form})


def form_students(request):
    if request.method == 'POST':
        min_length = 3
        my_form = Form_students(request.POST)
        if my_form.is_valid() \
                and len(my_form.cleaned_data['name']) >= min_length \
                and len(my_form.cleaned_data['last_name']) >= min_length \
                and len(my_form.cleaned_data['email']) >= min_length \
                and len(my_form.cleaned_data['username']) >= 8 \
                and len(my_form.cleaned_data['password']) >= 8:
            information = my_form.cleaned_data
            student = Student(name=information['name'].lower(),
                              second_name=information['second_name'].lower(),
                              last_name=information['last_name'].lower(),
                              second_last_name=information['second_last_name'].lower(),
                              email=information['email'].lower(),
                              username=information['username'].lower(),
                              password=information['password'])
            student.save()
            success_message = "Student Created"
            return render(request, "AppEdukate/redirect_forms.html", {"success_message": success_message})
        else:
            if not my_form.cleaned_data.get('name'):
                my_form.add_error('name', 'This field is required.')
            elif len(my_form.cleaned_data['name']) < min_length:
                my_form.add_error('name', f'The name must have more than {min_length} characters')

            if not my_form.cleaned_data.get('last_name'):
                my_form.add_error('last_name', 'This field is required.')
            elif len(my_form.cleaned_data['last_name']) < min_length:
                my_form.add_error('last_name', f'The last name must have more than {min_length} characters')

            if not my_form.cleaned_data.get('email'):
                my_form.add_error('email', 'This field is required.')
            elif len(my_form.cleaned_data['email']) < min_length:
                my_form.add_error('email', f'The email must have more than {min_length} characters')

            if not my_form.cleaned_data.get('username'):
                my_form.add_error('username', 'This field is required.')
            elif len(my_form.cleaned_data['username']) < 8:
                my_form.add_error('username', 'The username must have more than 8 characters')

            if not my_form.cleaned_data.get('password'):
                my_form.add_error('password', 'This field is required.')
            elif len(my_form.cleaned_data['password']) < 8:
                my_form.add_error('password', 'The password must have more than 8 characters')

    else:
        my_form = Form_students()
    return render(request, "AppEdukate/form_students.html", {"my_form": my_form})


def form_teachers(request):
    if request.method == 'POST':
        min_length = 3
        my_form = Form_teachers(request.POST)
        if my_form.is_valid() and len(my_form.cleaned_data['name']) >= min_length \
                and len(my_form.cleaned_data['last_name']) >= min_length \
                and len(my_form.cleaned_data['profession']) >= min_length:
            information = my_form.cleaned_data
            teacher = Teacher(name=information['name'].lower(), last_name=information['last_name'].lower(),
                              email=information['email'].lower(),
                              profession=information['profession'].lower())
            teacher.save()
            success_message = "Teacher Created"
            return render(request, "AppEdukate/redirect_forms.html", {"success_message": success_message})
        else:
            if len(my_form.cleaned_data['name']) < min_length:
                my_form.add_error('name', f'The name must have more than {min_length} characters')
            if len(my_form.cleaned_data['last_name']) < min_length:
                my_form.add_error('last_name', f'The last name must have more than {min_length} characters')
            if len(my_form.cleaned_data['email']) < min_length:
                my_form.add_error('email', f'The email must have more than {min_length} characters')
    else:
        my_form = Form_teachers()
    return render(request, "AppEdukate/form_teachers.html", {"my_form": my_form})


@login_required
def form_assignment(request):
    if request.method == 'POST':
        min_length = 3
        my_form = Form_assignment(request.POST)
        if my_form.is_valid() and len(my_form.cleaned_data['name']) >= min_length \
                and len(my_form.cleaned_data['last_name']) >= min_length \
                and len(my_form.cleaned_data['course']) >= min_length:
            information = my_form.cleaned_data
            assignment = Assignment(name=information['name'].lower(), last_name=information['last_name'].lower(),
                                    course=information['course'].lower(), commission=int(information['commission']),
                                    assignment_date=information['assignment_date'],
                                    assignment=bool(information['assignment']))
            assignment.save()
            success_message = "Assignment Loaded"
            return render(request, "AppEdukate/redirect_forms.html", {"success_message": success_message})
        else:
            if len(my_form.cleaned_data['name']) < min_length:
                my_form.add_error('name', f'The name must have more than {min_length} characters')
            if len(my_form.cleaned_data['last_name']) < min_length:
                my_form.add_error('last_name', f'The last name must have more than {min_length} characters')
            if len(my_form.cleaned_data['course']) < min_length:
                my_form.add_error('course', f'The course must have more than {min_length} characters')
    else:
        my_form = Form_assignment()
    return render(request, "AppEdukate/form_assignment.html", {"my_form": my_form})


##########################################
#            COURSES AVAIBLES            #
##########################################


def courses_avaibles(request):
    all_courses = Course.objects.all()
    course_counts = defaultdict(int)
    for course in all_courses:
        course_counts[course.name] += 1
    unique_courses = []
    for course_name, count in course_counts.items():
        unique_courses.append({
            "name": course_name.title(),
            "count": count
        })
    context = {
        "courses": unique_courses
    }
    return render(request, "AppEdukate/courses.html", context=context)
