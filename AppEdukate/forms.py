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
    first_name = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your first name.'})
    second_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your last name.'})
    second_last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True, error_messages={'required': 'Please enter your email.'})
    profession = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your profession.'})
    username = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your username.'})
    password = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your password.'})



class Form_assignment(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your first name.'})
    second_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True, error_messages={'required': 'Please enter your last name.'})
    second_last_name = forms.CharField(max_length=30, required=False)
    course = forms.CharField(required=True, error_messages={'required': 'Please enter your course.'})
    commission = forms.IntegerField(required=True, error_messages={'required': 'Please enter your commission.'})
    assignment_date = forms.DateField(input_formats=['%d/%m/%Y'], required=True, error_messages={'required': 'Please enter the assignment date.'})
    assignment = forms.BooleanField(required=False)
