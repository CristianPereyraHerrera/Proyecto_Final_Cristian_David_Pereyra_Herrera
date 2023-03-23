from django import forms


class Form_courses(forms.Form):
    course = forms.CharField()
    commission = forms.IntegerField()


class Form_students(forms.Form):
    name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    second_last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())


class Form_teachers(forms.Form):
    name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    second_last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    profession = forms.CharField(max_length=30)


class Form_assignment(forms.Form):
    name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    second_last_name = forms.CharField(max_length=30)
    course = forms.CharField()
    commission = forms.IntegerField()
    assignment_date = forms.DateField(input_formats=['%d/%m/%Y'])
    assignment = forms.BooleanField(required=False)
