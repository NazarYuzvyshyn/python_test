import random

from main.business_object.passenger import Passenger
from main.business_object.ticket import Ticket
from main.custom_utils.general_utils import get_url
from ..custom_utils.wait_utils import *
from ..custom_utils.web_elem_utils import *


class ResultsPage:
    def __init__(self, ticket: Ticket, passenger: Passenger):
        self.ticket = ticket
        self.passenger = passenger
        self.counter = 0

    def get_random_train(self):
        """ Gets random train from list of results after search
        and if trip is round write to Ticket object each one train name
        :return: index of this train in result list """
        trains_locator = "//*[contains(@class,'train') and not(contains(@class,'your'))]/strong"
        wait_list_elements("Trains", trains_locator, 10)
        trains = get_elements(By.XPATH, trains_locator)
        index = random.randint(trains.__len__() - 1)
        train_number = element_text_content(trains[index])
        info("--------------- Train -------------")
        info("Поезд: " + train_number)
        if self.counter == 0:
            self.ticket.train_number = train_number
        else:
            self.ticket.train_number_round = train_number
        return index

    def get_random_place_type(self, index):
        """ Uses train list index (see above),chooses block of categories which is related to this train.
        Can contains "Люкс","Купе","Плацкарт","Сидячий" (one of them or several)
        :param: index index of train in result list """
        place_category = "//*[contains(@class,'free-places') and preceding-sibling::*[contains(@class,'train')]]"
        block = "(%s)[%s]" % (place_category, index + 1)
        wait_list_elements("Place types", block, 5)
        type_names = get_elements(By.XPATH, block + "//span")
        type_index = random.randint(type_names.__len__())
        text = element_text_content(type_names[type_index])
        choose_type = "(%s//span/../a)[%s]" % (block, type_index + 1)
        click_on("Тип: " + text, By.XPATH, choose_type)
        if self.counter == 0:
            self.ticket.place_type = text
        else:
            self.ticket.place_type_round = text

    def get_random_place(self):
        """ Gets available free place in chosen train and place category."""
        free_places = "//*[contains(@class,'sits_block')]//a"
        wait_list_elements("Free places", free_places, 5)
        places = get_elements(By.XPATH, free_places)
        place_index = random.randint(places.__len__())
        text = element_text_content(places[place_index])
        place = "(%s)[%s]" % (free_places, place_index + 1)
        click_on("Место: " + text, By.XPATH, place)
        if self.counter == 0:
            self.ticket.place_number = text
        else:
            self.ticket.place_number_round = text

    def fill_passenger_form(self):
        last_name = "//*[contains(@id,'lastname')]"
        input_keys("Фамилия", By.XPATH, last_name, self.passenger.last_name)
        first_name = "//*[contains(@id,'firstname')]"
        input_keys("Имя", By.XPATH, first_name, self.passenger.first_name)
        self.ticket.last_and_first_names = self.passenger.last_name + " " + self.passenger.first_name

    def fill_contact_info(self):
        email = "//*[@id='user_form']//*[@id='email']"
        input_keys("Email", By.XPATH, email, self.passenger.email)
        phone = "//*[@id='buyer_data']//*[@id='phone_number']"
        input_keys("Номер телефона", By.XPATH, phone, self.passenger.phone)

    def accept_offerta(self):
        offerta = "//*[@id='i_accept_offerta']/.."
        click_on("Я принимаю правила публичной оферты", By.XPATH, offerta)

    def submit(self):
        price = "//*[contains(@class,'buy-block')]//strong[not(contains(@class,'old-price'))]"
        text = element_text_content(get_element(By.XPATH, price))
        if self.counter == 0:
            self.ticket.price = text
        else:
            self.ticket.price_round = text
        self.counter = 1
        current_url = get_url()
        info("-----------------------------------")
        submit = "//*[contains(@class,'buy-block')]//*[@type='submit']"
        click_on("Продолжить", By.XPATH, submit)
        wait_change_url(current_url, 30)
