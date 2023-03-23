from django.contrib import admin
from AppEdukate.models import Course, Student, Teacher, Assignment


# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Assignment)

