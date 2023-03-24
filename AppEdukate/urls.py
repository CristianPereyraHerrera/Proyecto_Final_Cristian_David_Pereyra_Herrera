from django.urls import path
from django.contrib.auth.decorators import login_required
from AppEdukate.views import index, about, detail, feature, team, testimonial, contact, courses, students, teachers, \
    search_courses, search_students, search_teachers, form_courses, form_students, form_teachers, form_assignment,\
    courses_avaibles


urlpatterns = [
    path('', index, name="AppEdukateIndex"),
    path('about/', about, name="AppEdukateAbout"),
    path('detail/', detail, name="AppEdukateDetail"),
    path('feature/', feature, name="AppEdukateFeature"),
    path('team/', team, name="AppEdukateTeam"),
    path('testimonial/', testimonial, name="AppEdukateTestimonial"),
    path('contact/', contact, name="AppEdukateContact"),

    path('courses/', courses, name="AppEdukateCourses"),
    path('students/', students, name="AppEdukateStudents"),
    path('teachers/', teachers, name="AppEdukateTeachers"),

    path('search_courses/', login_required(search_courses), name="AppEdukateSearchCourses"),
    path('search_students/', search_students, name="AppEdukateSearchStudents"),
    path('search_teachers/', login_required(search_teachers), name="AppEdukateSearchTeachers"),

    path('form_courses/', form_courses, name="AppEdukateFormCourses"),
    path('form_students/', form_students, name="AppEdukateFormStudents"),
    path('form_teachers/', form_teachers, name="AppEdukateFormTeachers"),
    path('form_assignment/', form_assignment, name="AppEdukateFormAssignments"),

    path('courses_avaibles/', courses_avaibles, name="AppEdukateCoursesAvaibles"),
]
