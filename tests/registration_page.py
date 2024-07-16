from pages.form_page import StudentRegistrationPage


def test_student_registration_form():
    registration_page = StudentRegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.type_first_name('Anna')
    registration_page.type_last_name('Fedorova')
    registration_page.type_email('email@mail.com')
    registration_page.select_gender('Female')
    registration_page.type_user_number('9001234567')
    registration_page.fill_date_of_birth('1982', 'March', '18')
    registration_page.type_subject('Computer Science')
    registration_page.type_hobbies('Sports', 'Reading')
    registration_page.upload_photo('photo.png')
    registration_page.type_address('Saint-Petersburg, 190000')
    registration_page.type_state('NCR')
    registration_page.type_city('Delhi')
    registration_page.element_submit_registration_form()

    # THEN
    registration_page.should_have_registered_user_with(
        'Anna Fedorova',
        'email@mail.com',
        'Female',
        '9001234567',
        '18 March,1982',
        'Computer Science',
        'Sports, Reading',
        'photo.png',
        'Saint-Petersburg, 190000',
        'NCR Delhi'
    )