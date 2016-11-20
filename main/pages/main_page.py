from selenium.webdriver.common.by import By

from main.business_object.ticket import Ticket
from main.custom_services.wait_services import wait_for_url, wait_element_visible
from ..custom_services.custom_logger import *
from ..custom_services.web_elem_services import *


class MainPage:
    def __init__(self, ticket: Ticket):
        self.ticket = ticket
        self.day = None

    def get_ticket(self):
        info("--------- Departure point ---------")
        trip_from = "//*[@id='from_name_as']"
        input_keys_with_enter("Откуда", By.XPATH, trip_from, self.ticket.forward_city)
        info("----------- Arrival point -----------")
        trip_to = "//*[@id='to_name']"
        input_keys_with_enter("Куда", By.XPATH, trip_to, self.ticket.backward_city)
        date_field = "//*[@id='departure_date']"
        self.__set_date(self.ticket.forward_date, date_field)
        self.ticket.get_info.append(self.day)

    def get_round_trip(self):
        round_trip = "//*[contains(@class,'iradio_minimal') and child::*[@id='round_trip']]"
        click_on("'В обе стороны'", By.XPATH, round_trip)
        date_field = "//*[@id='departure_date_back']"
        self.__set_date(self.ticket.backward_date, date_field)
        self.ticket.get_round_info.append(self.day)

    def __set_date(self, date, field):
        click_on("", By.XPATH, field)
        calendar = "//*[@id='ui-datepicker-div']"
        wait_element_visible("Calendar", By.XPATH, calendar, 5)
        day = str(date.day)
        self.day = " %s " % day
        month = str(date.month - 1)
        year = str(date.year)
        date_in_calendar = "//*[@data-year='" + year + "' and @data-month='" + month + "']/*[text()='" + day + "']"
        click_on(date.__str__(), By.XPATH, date_in_calendar)

    def search(self):
        submit = "//*[contains(@class,'main-search__block')]//*[@type='submit']"
        click_on("Поиск", By.XPATH, submit)
        wait_for_url("results", 15)
