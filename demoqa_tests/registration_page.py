import os

from selene import browser, by, have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_genter(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()

    def fill_date_of_birth(self, mm, yyyy, dd):
        browser.element('#dateOfBirthInput').click()
        browser.element("[class='react-datepicker__month-select']").click().element(by.text(mm)).click()
        browser.element("[class='react-datepicker__year-select']").click().element(by.text(yyyy)).click()
        browser.element(f"[class ='react-datepicker__day react-datepicker__day--0{dd}']").click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()

    def download_picture(self, path):
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"../resources/images/{path}"))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').click().element(by.text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click().element(by.text(value)).click()

    def submit(self):
        browser.element('#submit').click()


class TableResponsive:

    def assert_text(self, firstName, lastName, userEmail, genter, userNumber, day, month, year, subjects, hobbies,
                    images, currentAddress, state, city):
        browser.element(("[class='table-responsive']")).should(have.text(f'{firstName} {lastName}'))
        browser.element(("[class='table-responsive']")).should(have.text(userEmail))
        browser.element(("[class='table-responsive']")).should(have.text(genter))
        browser.element(("[class='table-responsive']")).should(have.text(userNumber))
        browser.element(("[class='table-responsive']")).should(have.text(f'{day} {month},{year}'))
        browser.element(("[class='table-responsive']")).should(have.text(subjects))
        browser.element(("[class='table-responsive']")).should(have.text(hobbies))
        browser.element(("[class='table-responsive']")).should(have.text(images))
        browser.element(("[class='table-responsive']")).should(have.text(currentAddress))
        browser.element(("[class='table-responsive']")).should(have.text(f'{state} {city}'))
