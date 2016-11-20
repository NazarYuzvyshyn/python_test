from main.custom_utils.constants import BASE_URL
from main.custom_utils.general_utils import go_to
from main.pages.main_page import MainPage


def test_001(web_driver):
    go_to(BASE_URL)

    main_page = MainPage()
    main_page.get_ticket()
    main_page.get_round_trip()
    main_page.search()

