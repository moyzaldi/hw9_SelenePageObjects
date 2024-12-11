import os

from selene import browser, by, have

from demoqa_tests.data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def register(self, value: User):
        browser.element('#firstName').type(value.first_name)
        browser.element('#lastName').type(value.last_name)
        browser.element('#userEmail').type(value.user_email)
        browser.element('#userNumber').type(value.user_number)
        browser.element('#genterWrapper').element(by.text(value.genter)).click()
        browser.element('#dateOfBirthInput').click()
        browser.element("[class='react-datepicker__month-select']").click().element(by.text(value.month)).click()
        browser.element("[class='react-datepicker__year-select']").click().element(by.text(value.year)).click()
        browser.element(f"[class ='react-datepicker__day react-datepicker__day--0{value.day}']").click()
        browser.element('#subjectsInput').type(value.subjects).press_enter()
        browser.element('#hobbiesWrapper').element(by.text(value.hobbies)).click()
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"../resources/images/{value.images}"))
        browser.element('#currentAddress').type(value.current_address)
        browser.element('#state').click().element(by.text(value.state)).click()
        browser.element('#city').click().element(by.text(value.city)).click()
        browser.element('#submit').click()

    def assert_text(self, value: User):
        browser.element(("[class='table-responsive']")).should(have.text(f'{value.first_name} {value.last_name}'))
        browser.element(("[class='table-responsive']")).should(have.text(value.last_name))
        browser.element(("[class='table-responsive']")).should(have.text(value.genter))
        browser.element(("[class='table-responsive']")).should(have.text(value.user_number))
        browser.element(("[class='table-responsive']")).should(have.text(f'{value.day} {value.month},{value.year}'))
        browser.element(("[class='table-responsive']")).should(have.text(value.subjects))
        browser.element(("[class='table-responsive']")).should(have.text(value.hobbies))
        browser.element(("[class='table-responsive']")).should(have.text(value.images))
        browser.element(("[class='table-responsive']")).should(have.text(value.current_address))
        browser.element(("[class='table-responsive']")).should(have.text(f'{value.state} {value.city}'))
