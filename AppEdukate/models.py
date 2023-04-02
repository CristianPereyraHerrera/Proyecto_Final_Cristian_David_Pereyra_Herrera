from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=30)
    commission = models.IntegerField(unique=True)

    def __str__(self):
        return f"Course: {self.name} ----- Commission: {self.commission}"


class Assignment(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    second_last_name = models.CharField(max_length=30, blank=True, null=True)
    course = models.CharField(max_length=30)
    commission = models.IntegerField()
    assignment_date = models.DateField()
    assignment = models.BooleanField()

    def __str__(self):
        return f"Assignment: {self.first_name} {self.second_name} {self.last_name} {self.second_last_name} " \
               f"----- Course: {self.course} ----- Commission: {self.commission} " \
               f"----- Assignment the day: {self.assignment_date} ----- Assignment: {self.assignment}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} ----- Email: {self.email}" \
               f" ----- Username: {self.username} ----- Password: {self.password}"
