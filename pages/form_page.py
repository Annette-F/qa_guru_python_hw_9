from pathlib import Path
from selene import browser, have
from test_data.users import User


class StudentRegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def type_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def type_email(self, mail):
        browser.element('#userEmail').type(mail)

    def select_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def type_user_number(self, user_number):
        browser.element('#userNumber').type(user_number)

    def date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element('[value="2"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element('[value="1982"]').click()
        browser.element('.react-datepicker__day--018').click()

    def type_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def type_hobbies(self, hobbies):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobbies)).click()

    def upload_photo(self, photo):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/{photo}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def type_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def element_submit_registration_form(self):
        browser.element('#submit').click()

    def should_have_registered_user_with(self, student):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student.first_name} {student.last_name}',
                f'{student.mail}',
                f'{student.gender}',
                f'{student.user_number}',
                f'{student.date_of_birth}',
                f'{student.subject}',
                f'{student.hobbies}',
                f'{student.photo}',
                f'{student.address}',
                f'{student.state} {student.city}'
            )
        )

    def register(self, student: User):
        self.type_first_name(student.first_name)
        self.type_last_name(student.last_name)
        self.type_email(student.mail)
        self.select_gender(student.gender)
        self.type_user_number(student.user_number)
        self.date_of_birth()
        self.type_subject(student.subject)
        self.type_hobbies(student.hobbies)
        self.upload_photo(student.photo)
        self.type_address(student.address)
        self.type_state(student.state)
        self.type_city(student.city)
        self.element_submit_registration_form()

