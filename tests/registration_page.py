from selene import browser, have
import os


def test_filling_and_sending_input():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Anna')
    browser.element('#lastName').type('Fedorova')
    browser.element('#userEmail').type('email@mail.com')
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').type('9001234567')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('[value = "1982"]').click()
    browser.element('.react-datepicker__month-select').element('[value = "2"]').click()
    browser.element('.react-datepicker__day--018').click()
    browser.element('#subjectsInput').type('comp').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo.png'))
    browser.element('#currentAddress').type('Saint-Petersburg, 190000')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts(
        'Anna Fedorova', 'email@mail.com', 'Female', '9001234567', '18 March,1982',
        'Computer Science', 'Sports, Reading', 'photo.png', 'Saint-Petersburg, 190000', 'NCR Delhi'))

