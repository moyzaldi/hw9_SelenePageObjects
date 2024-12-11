from demoqa_tests.data.users import  registered_user
from demoqa_tests.registration_page import RegistrationPage, TableResponsive


def test_type_registration_form(browser_settings):
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name(registered_user.first_name)
    registration_page.fill_last_name(registered_user.last_name)
    registration_page.fill_email(registered_user.user_email)
    registration_page.fill_genter(registered_user.genter)
    registration_page.fill_mobile(registered_user.user_number)
    registration_page.fill_date_of_birth(registered_user.month, registered_user.year, registered_user.day)
    registration_page.fill_subjects(registered_user.subjects)
    registration_page.fill_hobbies(registered_user.hobbies)
    registration_page.download_picture(registered_user.images)
    registration_page.fill_current_address(registered_user.current_address)
    registration_page.fill_state(registered_user.state)
    registration_page.fill_city(registered_user.city)
    registration_page.submit()

    table_responsive = TableResponsive()

    table_responsive.assert_text(registered_user.first_name, registered_user.last_name, registered_user.user_email,
                                 registered_user.genter, registered_user.user_number, registered_user.day, registered_user.month,
                                 registered_user.year, registered_user.subjects,
                                 registered_user.hobbies,
                                 registered_user.images, registered_user.current_address, registered_user.state, registered_user.city)
