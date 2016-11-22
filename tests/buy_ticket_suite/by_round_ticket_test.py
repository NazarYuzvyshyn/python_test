from main.business_object.passenger import Passenger
from main.business_object.ticket import Ticket
from main.custom_services.constants import BASE_URL, LIQPAY
from main.custom_services.general_services import go_to, get_url
from main.pages.main_page import MainPage
from main.pages.purchase_page import PayBy
from main.pages.purchase_page import PurchasePage
from main.pages.results_page import ResultsPage
from tests.custom_logger import info_test


def test_001(web_driver, end):
    ticket = Ticket("ticket")
    passenger = Passenger("passenger")
    info_test("test")
    go_to(BASE_URL)

    main_page = MainPage(ticket)
    main_page.get_ticket()
    main_page.get_round_trip()
    main_page.search()

    result_page = ResultsPage(ticket, passenger)
    result_page.get_random_train()
    result_page.get_random_place_type()
    result_page.get_random_place()
    result_page.fill_passenger_form()
    result_page.fill_contact_info()
    result_page.accept_offerta()
    result_page.submit()

    #  Round ticket buying
    result_page.get_random_train()
    result_page.get_random_place_type()
    result_page.get_random_place()
    result_page.submit()

    purchase_page = PurchasePage(ticket)
    assert purchase_page.check_ticket_info(ticket.get_info) is True
    assert purchase_page.check_ticket_info(ticket.get_round_info) is True
    assert purchase_page.get_price() <= ticket.price + ticket.round_price

    purchase_page.pay(PayBy.PRIVAT_24)
    purchase_page.submit()
    assert LIQPAY in get_url()
