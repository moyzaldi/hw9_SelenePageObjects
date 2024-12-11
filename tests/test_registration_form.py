from demoqa_tests.data.users import registered_user
from demoqa_tests.registration_page import RegistrationPage



def test_registers_user(browser_settings):
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(registered_user)
    registration_page.assert_text(registered_user)

