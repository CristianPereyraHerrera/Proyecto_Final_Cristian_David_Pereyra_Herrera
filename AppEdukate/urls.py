from django.urls import path
from AppEdukate.views import index, about, detail, feature, team, testimonial, contact, search_courses, \
    search_students, form_courses, form_students, form_assignment, courses_avaibles, page_not_avaible


urlpatterns = [
    path('', index, name="AppEdukateIndex"),
    path('about/', about, name="AppEdukateAbout"),
    path('detail/', detail, name="AppEdukateDetail"),
    path('feature/', feature, name="AppEdukateFeature"),
    path('team/', team, name="AppEdukateTeam"),
    path('testimonial/', testimonial, name="AppEdukateTestimonial"),
    path('contact/', contact, name="AppEdukateContact"),

    path('search_courses/', search_courses, name="AppEdukateSearchCourses"),
    path('search_students/', search_students, name="AppEdukateSearchStudents"),

    path('form_courses/', form_courses, name="AppEdukateFormCourses"),
    path('form_students/', form_students, name="AppEdukateFormStudents"),
    path('form_assignment/', form_assignment, name="AppEdukateFormAssignments"),

    path('courses_avaibles/', courses_avaibles, name="AppEdukateCoursesAvaibles"),

    path('page_not_avaible/', page_not_avaible, name="AppEdukatePageNotAvaible"),

]
