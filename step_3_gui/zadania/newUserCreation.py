from time import sleep

from faker import Faker
from selene import config, browser
from selene.conditions import visible, clickable
from selene.support.jquery_style_selectors import s


class User:
    def __init__(self, username, password, email):
        self.email = email
        self.password = password
        self.username = username


class HeaderBar:
    def __init__(self):
        self.sign_in_button = s("//*[text()='Sign In']")
        self.__join_button = s("gg-menu-nav-nouser a[href='/join']")

    def go_to_sign_in(self):
        self.sign_in_button.click()

    def go_to_user_registration(self):
        self.__join_button.click()


class SignInModel:
    def __init__(self):
        self.__user_name_field = s("#inputUsername")
        self.__password_field = s("#inputPassword")
        self.__sign_in_button = s("//*[text()='Sign In']")

    def login(self, user: User):
        self.__user_name_field.type(user.username)
        self.__password_field.type(user.password)


class RegistrationForm:
    def __init__(self):
        self.__user_name_field = s("#join-username")
        self.__password_field = s("#join-password")
        self.__email_field = s("#join-email")
        self.__submit_button = s("[type='submit']")

    def fill_user_data(self, user_data: User):  #: str   will add hint to the code
        self.__user_name_field.type(user_data.username)
        self.__password_field.type(user_data.password)
        self.__email_field.type(user_data.email)


faker = Faker()
env = f"http://boardgamegeek.com/"
config.timeout = 5
config.start_maximized = True

myUser = User('StevenzUsZe', '0Ludu8Xk)_', 'thomascody@alexander.org')
myHeader = HeaderBar()
browser.open_url(env)
sleep(1)
accept_cookie_button = s("#c-p-bn")
accept_cookie_button.click()
accept_cookie_button.should_not_be(visible)



# myHeader.go_to_user_registration()
myHeader.go_to_user_registration()

myRegistration = RegistrationForm()
myRegistration.fill_user_data(myUser)

sleep(5)

#
# register_button_click = s("gg-menu-nav-nouser a[href='/join']")
# registration_username_field = s("#join-username")
# registration_password_field = s("#join-password")
# registration_email_field = s("#join-email")
# registration_submit_button = s("[type='submit']")
# accept_cookie_button = s("#c-p-bn")
#
# username = faker.first_name() + "".join(faker.random_letters(length=5))
# password = faker.password(length=10)
# email = faker.ascii_email()
#
# # open browser
# browser.open_url(env)
# register_button_click.should_be(clickable)
#
# accept_cookie_button.should_be(clickable)
# sleep(1)
# accept_cookie_button.click()
# accept_cookie_button.should_not_be(visible)
#
# # click on registration and wait for form to be loaded
# register_button_click.click()
# registration_submit_button.should_be(clickable)
#
# # enter fields' values and submit
# registration_username_field.type(username)
# registration_password_field.type(password)
# registration_email_field.type(email).submit()
# s("//*[normalize-space()='Skip']").click()
#
# sleep(5)
