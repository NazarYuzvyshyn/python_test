from main.business_objects.ticket import Ticket
from main.custom_services.wait_services import wait_for_url, wait_element_visible
from ..custom_services.element_services import *


class MainPage:
    def __init__(self, ticket: Ticket):
        self.ticket = ticket
        self.day = None

    def set_route_and_date(self):
        info("--------- Departure point ---------")
        trip_from = "from_name_as"
        input_keys_with_enter("Откуда", By.ID, trip_from, self.ticket.forward_city)
        info("----------- Arrival point -----------")
        trip_to = "to_name"
        input_keys_with_enter("Куда", By.ID, trip_to, self.ticket.backward_city)
        date_field = "departure_date"
        self.__set_date(self.ticket.forward_date, date_field)
        self.ticket.get_info.append(self.day)

    def set_round_trip(self):
        round_trip = "//*[contains(@class,'iradio_minimal') and child::*[@id='round_trip']]"
        click_on("'В обе стороны'", By.XPATH, round_trip)
        date_field = "departure_date_back"
        self.__set_date(self.ticket.backward_date, date_field)
        self.ticket.get_round_info.append(self.day)

    def __set_date(self, date, field):
        click_on("", By.ID, field)
        calendar = "ui-datepicker-div"
        wait_element_visible("Calendar", By.ID, calendar, 5)
        day = str(date.day)
        self.day = " %s " % day
        month = str(date.month - 1)
        year = str(date.year)
        date_in_calendar = "//*[@data-year='%s' and @data-month='%s']/*[text()='%s']" % (year, month, day)
        click_on(date.__str__(), By.XPATH, date_in_calendar)

    def search(self):
        submit = "//*[contains(@class,'main-search__block')]//*[@type='submit']"
        click_on("Поиск", By.XPATH, submit)
        wait_for_url("results", 15)
