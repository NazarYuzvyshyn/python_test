from nose.tools import *

from main.business_object.user import User
from main.custom_utils.constants import *
from main.custom_utils.general_servise import get_url, page_url, is_in, is_equal
from main.pages.main_page import MainPage
from main.pages.profile_page import ProfilePage
from main.pages.regiter_page import RegisterPage


def test_002(web_driver):
    pass
    message = "profile"

    get_url(BASE_URL)

    main_page = MainPage()
    main_page.goto_register_page()

    register_page = RegisterPage()
    user = User("user_for_register")
    register_page.fill_register_form(user)
    register_page.submit()

    is_in(message, page_url())

    profile_page = ProfilePage()

    is_equal(user.email, profile_page.user_email())

