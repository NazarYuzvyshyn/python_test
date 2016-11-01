from main.base_class import BaseClass
from main.business_object.user import User
from main.pages.main_page import MainPage
from main.custom_utils.general_servise import get_url
from main.custom_utils.constants import *
from main.pages.regiter_page import RegisterPage


def test_001(web_driver):

    BaseClass(web_driver)

    get_url(BASE_URL)

    main_page = MainPage()
    main_page.goto_register_page()

    register_page = RegisterPage()
    user = User("user_for_register")
    register_page.fill_register_form(user)
    register_page.submit_register()