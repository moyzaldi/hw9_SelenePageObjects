from demoqa_tests.resourse import RegistrationPage, TableResponsive

firstName = 'Anna'
lastName = 'Ivanova'
userEmail = 'test@test.com'
userNumber = '1111111111'

month = 'June'
year = '2000'
day = '01'

genter = 'Female'
hobbies = 'Reading'

images = 'butterflies.png'
currentAddress = 'Russia'
subjects = 'Computer Science'

state = 'Uttar Pradesh'
city = 'Merrut'


def test_type_registration_form(browser_settings):
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name(firstName)
    registration_page.fill_last_name(lastName)
    registration_page.fill_email(userEmail)
    registration_page.fill_genter(genter)
    registration_page.fill_mobile(userNumber)
    registration_page.fill_date_of_birth(month, year, day)
    registration_page.fill_subjects(subjects)
    registration_page.fill_hobbies(hobbies)
    registration_page.download_picture(images)
    registration_page.fill_current_address(currentAddress)
    registration_page.fill_state(state)
    registration_page.fill_city(city)
    registration_page.submit()

    table_responsive = TableResponsive()

    table_responsive.assert_text(firstName, lastName, userEmail, genter, userNumber, day, month, year, subjects,
                                 hobbies,
                                 images, currentAddress, state, city)
