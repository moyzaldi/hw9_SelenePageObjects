from demoqa_tests.data.users import registered_user
from demoqa_tests.registration_page import RegistrationPage, TableResponsive


def test_registration_user(browser_settings):
    registration_page = RegistrationPage()



    table_responsive = TableResponsive()

    table_responsive.assert_text(registered_user.first_name, registered_user.last_name, registered_user.user_email,
                                 registered_user.genter, registered_user.user_number, registered_user.day,
                                 registered_user.month,
                                 registered_user.year, registered_user.subjects,
                                 registered_user.hobbies,
                                 registered_user.images, registered_user.current_address, registered_user.state,
                                 registered_user.city)
