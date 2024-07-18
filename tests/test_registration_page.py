from pages.form_page import StudentRegistrationPage
from test_data.users import User


def test_student_registration():
    student = User(first_name='Anna',
                   last_name='Fedorova',
                   mail='email@mail.com',
                   gender='Female',
                   user_number='9001234567',
                   date_of_birth='18 March,1982',
                   subject='Computer Science',
                   hobbies='Sports',
                   photo='photo.png',
                   address='Saint-Petersburg, 190000',
                   state='NCR',
                   city='Delhi')
    form_page = StudentRegistrationPage()
    form_page.open()
    form_page.register(student)
    form_page.should_have_registered_user_with(student)
