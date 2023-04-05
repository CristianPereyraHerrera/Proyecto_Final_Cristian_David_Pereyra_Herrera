from django.contrib.auth.models import User
from django.test import TestCase
from AppEdukate.forms import Form_assignment
from AppEdukate.models import Course


# Create your tests here.
class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name="python", commission=777111)
        Course.objects.create(name="data", commission=777222)
        Course.objects.create(name="java", commission=777333)

    def test_create_courses(self):
        p1 = Course.objects.get(commission=777111)
        p2 = Course.objects.get(commission=777222)
        p3 = Course.objects.get(commission=777333)
        self.assertEqual(p1.name, 'python')
        self.assertEqual(p2.name, 'data')
        self.assertEqual(p3.name, 'java')


class FormAssignmentTest(TestCase):
    def test_valid_form(self):          # envía un conjunto de datos válidos al formulario Form_assignment y
        form_data = {                   # verifica que el formulario sea válido.
            'first_name': 'John',
            'last_name': 'Doe',
            'link_assignment': 'https://google.com',
            'course': 'python',
            'commission': 111111,
            'assignment_date': '04/04/2023',
            'assignment': True,
        }
        form = Form_assignment(data=form_data)
        self.assertTrue(form.is_valid())

    def test_required_fields(self):     # se verifica que el formulario no sea válido cuando se
        form_data = {                   # dejan en blanco los campos requeridos.
            'first_name': '',
            'last_name': '',
            'link_assignment': '',
            'course': '',
            'commission': '',
            'assignment_date': '',
        }
        form = Form_assignment(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    def test_invalid_date_format(self):   # se envía una fecha con un formato incorrecto y se verifica que el
        form_data = {                     # formulario no sea válido debido a la validación fallida del campo de fecha.
            'first_name': 'John',
            'last_name': 'Doe',
            'link_assignment': 'https://google.com',
            'course': 'data',
            'commission': 777222,
            'assignment_date': '04-04-2023',
            'assignment': True,
        }
        form = Form_assignment(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['assignment_date'][0], 'Enter a valid date (DD/MM/YYYY).')


class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='juancho',                      # Se prueba el método __str__ de la clase Student.
            last_name='montes',                        # se verifica que el método __str__ del objeto Student devuelva
            email='juanchomontes@gmail.com',          # una cadena de texto con los valores esperados
            username='usuario10',
            password='password10'
        )

    def test_user_str(self):
        self.assertEqual(str(self.user),
                         'Student: juancho montes ----- Email: juanchomontes@gmail.com ----- Username: usuario10 ----- Password: password10')


