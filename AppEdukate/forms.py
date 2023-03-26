from django import forms


class Form_courses(forms.Form):
    course = forms.CharField(required=True, error_messages={'required': 'Please enter a course.'})
    commission = forms.IntegerField(required=True, error_messages={'required': 'Please enter a commission.'})


class Form_students(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your first name.'})
    second_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your last name.'})
    second_last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True, error_messages={'required': 'Please enter your email.'})
    username = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your username.'})
    password = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your password.'})


class Form_teachers(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    second_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True)
    second_last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=30, required=True)
    profession = forms.CharField(max_length=30, required=True)


class Form_assignment(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    second_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True)
    second_last_name = forms.CharField(max_length=30, required=False)
    course = forms.CharField(required=True)
    commission = forms.IntegerField(required=True)
    assignment_date = forms.DateField(input_formats=['%d/%m/%Y'], required=True)
    assignment = forms.BooleanField(required=False)
