import pytest
from pages import Home

EMAIL = 'pizzade@yopmail.com'
PASSWORD = 'Qwerty123'


@pytest.allure.feature('Pizza.de')
@pytest.allure.story('Test Login')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
@pytest.mark.parametrize('email,password,result,description',
                         [(EMAIL, PASSWORD, True, 'correct credentials'),
                          (EMAIL, 'IncorrectPassword', False, 'correct email and incorrect password'),
                          ('incorrect@log.in', PASSWORD, False, 'incorrect email and correct password'),
                          ('incorrect@log.in', 'IncorrectPassword', False, 'incorrect email and password')])
def test_pizzade_login(driver, email, password, result, description):

    with pytest.allure.step('1. Open "Pizza.de" homepage'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('1. Click "Einloggen" (Login) button'):
        home.einloggen()

    with pytest.allure.step('2. Log in with: {}'.format(description)):

        login_result = home.login(email, password)
        assert login_result == result, 'Actual/expected Log in result: "{}"/"{}" for email/password: "{}"/"{}"'.format(
            login_result, result, email, password)
