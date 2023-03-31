from django.shortcuts import render
from collections import defaultdict
from AppEdukate.models import Course, Student, Assignment
from AppEdukate.forms import Form_courses, Form_students, Form_assignment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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


def page_not_avaible(request):
    return render(request, "AppEdukate/page_not_avaible.html")


##########################################
#                SEARCH                  #
##########################################


@login_required
def search_courses(request):
    name = request.GET.get('name')
    commission = request.GET.get('commission')
    min_length = 3
    courses = Course.objects.all()
    message_error = ""
    if not name and not commission and not request.GET:
        return render(request, "AppEdukate/search_courses.html")
    if not name and not commission:
        message_error = "Enter some data. Try Again"
        return render(request, "AppEdukate/search_courses.html", {'message_error': message_error})
    if name and len(name) < min_length or commission and len(commission) < min_length:
        message_error = f'You must enter at least {min_length} characters'
    else:
        if name:
            courses = courses.filter(name__icontains=name)
        elif commission:
            courses = courses.filter(commission=commission)
    if message_error:
        return render(request, "AppEdukate/search_courses.html", {'message_error': message_error})
    elif courses.exists():
        return render(request, "AppEdukate/search_courses.html", {'courses': courses, 'commission': commission})
    else:
        message_error = "No results found"
        return render(request, "AppEdukate/search_courses.html", {'message_error': message_error})


@login_required
def search_students(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    min_length = 3
    students = Student.objects.all()
    message_error = ""
    if not first_name and not last_name and not email and not request.GET:
        return render(request, "AppEdukate/search_students.html")
    if not first_name and not last_name and not email:
        message_error = "Enter some data. Try Again"
        return render(request, "AppEdukate/search_students.html", {'message_error': message_error})
    if first_name and len(first_name) < min_length:
        message_error = f"The name must have at least {min_length} characters."
        return render(request, "AppEdukate/search_students.html", {'message_error': message_error})
    if last_name and len(last_name) < min_length:
        message_error = f"The last name must have at least {min_length} characters."
        return render(request, "AppEdukate/search_students.html", {'message_error': message_error})
    if email and len(email) < min_length:
        message_error = f"The email must have at least {min_length} characters."
        return render(request, "AppEdukate/search_students.html", {'message_error': message_error})
    else:
        if first_name:
            students = students.filter(first_name__icontains=first_name.lower())
        if last_name:
            students = students.filter(last_name__icontains=last_name.lower())
        if email:
            students = students.filter(email__icontains=email.lower())
    if message_error:
        return render(request, "AppEdukate/search_students.html", {'message_error': message_error})
    elif students.exists():
        return render(request, "AppEdukate/search_students.html", {'students': students, 'last_name': last_name, 'email': email, 'message_error': message_error})
    else:
        message_error = "No results found"
        return render(request, "AppEdukate/search_students.html", {'message_error': message_error})


# @login_required
# def search_teachers(request):
#     first_name = request.GET.get('first_name')
#     last_name = request.GET.get('last_name')
#     email = request.GET.get('email')
#     profession = request.GET.get('profession')
#     min_length = 3
#     teachers = Teacher.objects.all()
#     message_error = ""
#     if not first_name and not last_name and not email and not profession and not request.GET:
#         return render(request, "AppEdukate/search_teachers.html")
#
#     if not first_name and not last_name and not email and not profession:
#         message_error = "Enter some data. Try Again"
#         return render(request, "AppEdukate/search_teachers.html", {'message_error': message_error})
#
#     if first_name and len(first_name) < min_length:
#         message_error = f"The name must have at least {min_length} characters."
#         return render(request, "AppEdukate/search_teachers.html", {'message_error': message_error})
#
#     if last_name and len(last_name) < min_length:
#         message_error = f"The last name must have at least {min_length} characters."
#         return render(request, "AppEdukate/search_teachers.html", {'message_error': message_error})
#
#     if email and len(email) < min_length:
#         message_error = f"The email must have at least {min_length} characters."
#         return render(request, "AppEdukate/search_teachers.html", {'message_error': message_error})
#
#     if profession and len(profession) < min_length:
#         message_error = f"The profession must have at least {min_length} characters."
#         return render(request, "AppEdukate/search_teachers.html", {'message_error': message_error})
#     else:
#         if first_name:
#             teachers = teachers.filter(first_name__icontains=first_name.lower())
#         if last_name:
#             teachers = teachers.filter(last_name__icontains=last_name.lower())
#         if email:
#             teachers = teachers.filter(email__icontains=email.lower())
#         if profession:
#             teachers = teachers.filter(profession__icontains=profession.lower())
#     if message_error:
#         return render(request, "AppEdukate/search_teachers.html", {'message_error': message_error})
#     elif teachers.exists():
#         return render(request, "AppEdukate/search_teachers.html", {'teachers': teachers, 'last_name': last_name, 'email': email, 'message_error': message_error})
#     else:
#         message_error = "No results found"
#         return render(request, "AppEdukate/search_teachers.html", {'message_error': message_error})


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
            commission = information['commission']

            if Course.objects.filter(commission=commission).exists():
                my_form.add_error('commission', 'Commission already exists')
            else:
                course = Course(name=information['course'].lower(), commission=commission)
                course.save()
                success_message = "Course Created Successfully!"
                return render(request, "AppEdukate/redirect_forms.html", {"success_message": success_message})
        else:
            if not my_form.cleaned_data.get('course'):
                my_form.add_error('course', 'This field is required.')
            elif len(my_form.cleaned_data['course']) < min_length:
                my_form.add_error('course', f'The course name must have more than {min_length} characters')

            if not my_form.cleaned_data.get('commission'):
                my_form.add_error('commission', 'This field is required.')
    else:
        my_form = Form_courses()
    return render(request, "AppEdukate/form_courses.html", {"my_form": my_form})


def form_students(request):
    if request.method == 'POST':
        min_length = 3
        my_form = Form_students(request.POST)
        if my_form.is_valid() \
                and len(my_form.cleaned_data['first_name']) >= min_length \
                and len(my_form.cleaned_data['last_name']) >= min_length \
                and len(my_form.cleaned_data['email']) >= min_length \
                and len(my_form.cleaned_data['username']) >= 8 \
                and len(my_form.cleaned_data['password']) >= 8:
            information = my_form.cleaned_data
            existing_user_email = User.objects.filter(email=information['email'].lower()).first()
            existing_user_username = User.objects.filter(username=information['username'].lower()).first()
            if existing_user_email:
                my_form.add_error('email', 'Email already exists')

            if existing_user_username:
                my_form.add_error('username', 'Username already exists')

            if existing_user_email or existing_user_username:
                return render(request, "AppEdukate/form_students.html", {"my_form": my_form})

            user = User.objects.create_user(username=information['username'].lower(),
                                            email=information['email'].lower(),
                                            password=information['password'],
                                            first_name=information.get('first_name', '').lower(),
                                            last_name=information.get('last_name', '').lower())
            user.save()
            success_message = "Student Created Successful!"
            return render(request, "AppEdukate/redirect_forms.html", {"success_message": success_message})
        else:
            if not my_form.cleaned_data.get('first_name'):
                my_form.add_error('first_name', 'This field is required.')
            elif len(my_form.cleaned_data['first_name']) < min_length:
                my_form.add_error('first_name', f'The name must have more than {min_length} characters')

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


# def form_teachers(request):
#     if request.method == 'POST':
#         min_length = 3
#         my_form = Form_teachers(request.POST)
#         if my_form.is_valid() \
#                 and len(my_form.cleaned_data['first_name']) >= min_length \
#                 and len(my_form.cleaned_data['last_name']) >= min_length \
#                 and len(my_form.cleaned_data['email']) >= min_length \
#                 and len(my_form.cleaned_data['profession']) >= min_length \
#                 and len(my_form.cleaned_data['username']) >= 8 \
#                 and len(my_form.cleaned_data['password']) >= 8:
#             information = my_form.cleaned_data
#
#             existing_user_email = User.objects.filter(email=information['email'].lower()).first()
#             existing_user_username = User.objects.filter(username=information['username'].lower()).first()
#
#             if existing_user_email:
#                 my_form.add_error('email', 'Email already exists')
#
#             if existing_user_username:
#                 my_form.add_error('username', 'Username already exists')
#
#             if existing_user_email or existing_user_username:
#                 return render(request, "AppEdukate/form_students.html", {"my_form": my_form})
#
#             user = User.objects.create_user(username=information['username'].lower(),
#                                             email=information['email'].lower(),
#                                             password=information['password'],
#                                             first_name=information.get('first_name', '').lower(),
#                                             last_name=information.get('last_name', '').lower())
#             teacher = Teacher(user=user,
#                               first_name=information.get('first_name', '').lower(),
#                               second_name=information.get('second_name', '').lower(),
#                               last_name=information.get('last_name', '').lower(),
#                               second_last_name=information.get('second_last_name', '').lower(),
#                               email=information['email'].lower(),
#                               profession=information.get('profession', '').lower(),
#                               username=information['username'].lower(),
#                               password=information['password'])
#             teacher.save()
#             success_message = "Teacher Created Successful!"
#             return render(request, "AppEdukate/redirect_forms.html", {"success_message": success_message})
#         else:
#             if not my_form.cleaned_data.get('first_name'):
#                 my_form.add_error('first_name', 'This field is required.')
#             elif len(my_form.cleaned_data['first_name']) < min_length:
#                 my_form.add_error('first_name', f'The name must have more than {min_length} characters')
#
#             if not my_form.cleaned_data.get('last_name'):
#                 my_form.add_error('last_name', 'This field is required.')
#             elif len(my_form.cleaned_data['last_name']) < min_length:
#                 my_form.add_error('last_name', f'The last name must have more than {min_length} characters')
#
#             if not my_form.cleaned_data.get('email'):
#                 my_form.add_error('email', 'This field is required.')
#             elif len(my_form.cleaned_data['email']) < min_length:
#                 my_form.add_error('email', f'The email must have more than {min_length} characters')
#
#             if not my_form.cleaned_data.get('profession'):
#                 my_form.add_error('profession', 'This field is required.')
#             elif len(my_form.cleaned_data['profession']) < min_length:
#                 my_form.add_error('profession', f'The last name must have more than {min_length} characters')
#
#             if not my_form.cleaned_data.get('username'):
#                 my_form.add_error('username', 'This field is required.')
#             elif len(my_form.cleaned_data['username']) < 8:
#                 my_form.add_error('username', 'The username must have more than 8 characters')
#
#             if not my_form.cleaned_data.get('password'):
#                 my_form.add_error('password', 'This field is required.')
#             elif len(my_form.cleaned_data['password']) < 8:
#                 my_form.add_error('password', 'The password must have more than 8 characters')
#     else:
#         my_form = Form_teachers()
#     return render(request, "AppEdukate/form_teachers.html", {"my_form": my_form})


@login_required
def form_assignment(request):
    if request.method == 'POST':
        min_length = 3
        my_form = Form_assignment(request.POST)
        if my_form.is_valid() \
                and len(my_form.cleaned_data['first_name']) >= min_length \
                and len(my_form.cleaned_data['last_name']) >= min_length \
                and len(my_form.cleaned_data['course']) >= min_length:
            information = my_form.cleaned_data
            course_name = information['course'].lower()
            commission = information['commission']
            course_exists = Course.objects.filter(name__iexact=course_name, commission=commission).exists()
            commission_exists = Course.objects.filter(commission=commission).exists()
            if not commission_exists:
                my_form.add_error('commission', 'This commission does not exist in the database.')
            elif not course_exists:
                my_form.add_error('course', 'This course does not exist with this commission.')

            if course_exists:
                assignment = Assignment(first_name=information['first_name'].lower(),
                                        last_name=information['last_name'].lower(),
                                        course=course_name,
                                        commission=commission,
                                        assignment_date=information['assignment_date'],
                                        assignment=bool(information['assignment']))
                assignment.save()
                success_message = "Assignment Loaded Successful!"
                return render(request, "AppEdukate/redirect_forms.html", {"success_message": success_message})
            else:
                error_message = "Course and commission do not match."
                return render(request, "AppEdukate/form_assignment.html", {"my_form": my_form, "error_message": error_message})
        else:
            if not my_form.cleaned_data.get('first_name'):
                my_form.add_error('first_name', 'This field is required.')
            elif len(my_form.cleaned_data['first_name']) < min_length:
                my_form.add_error('first_name', f'The name must have more than {min_length} characters')

            if not my_form.cleaned_data.get('last_name'):
                my_form.add_error('last_name', 'This field is required.')
            elif len(my_form.cleaned_data['last_name']) < min_length:
                my_form.add_error('last_name', f'The last name must have more than {min_length} characters')

            if not my_form.cleaned_data.get('course'):
                my_form.add_error('course', 'This field is required.')
            elif len(my_form.cleaned_data['course']) < min_length:
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


##########################################
#                 BLOG                   #
##########################################


@login_required()
def blog(request):
    pass
