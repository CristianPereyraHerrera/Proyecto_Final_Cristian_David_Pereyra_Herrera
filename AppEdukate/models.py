from django.db import models




class Course(models.Model):
    name = models.CharField(max_length=30)
    commission = models.IntegerField(unique=True)

    def __str__(self):
        return f"Course: {self.name} ----- Commission: {self.commission}"


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    second_last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    commission = models.IntegerField()
    assignment_date = models.DateField()
    assignment = models.BooleanField()

    def __str__(self):
        return f"Assignment: {self.name} {self.second_name} {self.last_name} {self.second_last_name} " \
               f"----- Course: {self.course} ----- Commission: {self.commission} " \
               f"----- Assignment the day: {self.assignment_date} ----- Assignment: {self.assignment}"


class Student(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    second_last_name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


    def __str__(self):
        return f"Student: {self.name} {self.second_name} {self.last_name} {self.second_last_name} " \
               f"----- Email: {self.email} ----- Username: {self.username} ----- Password: {self.password}"


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    second_last_name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)

    def __str__(self):
        return f"Teacher: {self.name} {self.second_name} {self.last_name} {self.second_last_name} " \
               f"----- Email: {self.email} ----- Username: {self.username} ----- Password: {self.password}" \
               f" ----- Profession: {self.profession}"

