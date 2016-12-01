import random

from main.business_object.passenger import Passenger
from main.business_object.ticket import Ticket
from main.custom_services.general_services import get_url, clear_price
from ..custom_services.wait_services import *
from ..custom_services.element_services import *


class ResultsPage:
    def __init__(self, ticket: Ticket, passenger: Passenger):
        self.ticket = ticket
        self.passenger = passenger
        self.counter = 0
        self.index = None

    def get_random_train(self):
        """ Gets random train from list of results after search
        and if trip is round write to Ticket object each one train name """
        trains_locator = "//*[contains(@class,'train') and not(contains(@class,'your'))]/strong"
        wait_list_elements("Trains", By.XPATH, trains_locator, 10)
        trains = get_elements(By.XPATH, trains_locator)
        self.index = random.randint(0, trains.__len__() - 1)
        train_number = element_text_content(trains[self.index])
        info("--------------- Train -------------")
        info("Поезд: " + train_number)
        if self.counter == 0:
            self.ticket.get_info.append(train_number[:4])
        else:
            self.ticket.get_round_info.append(train_number[:4])

    def get_random_place_type(self):
        """ Uses train list index (see above),chooses block of categories which is related to this train.
        Can contains "Люкс","Купе","Плацкарт","Сидячий" (one of them or several) """
        place_category = "//*[contains(@class,'free-places') and preceding-sibling::*[contains(@class,'train')]]"
        block = "(%s)[%s]" % (place_category, self.index + 1)
        wait_list_elements("Place types", By.XPATH, block, 5)
        type_names = get_elements(By.XPATH, block + "//span")
        type_index = random.randint(0, type_names.__len__() - 1)
        text = element_text_content(type_names[type_index])
        choose_type = "(%s//span/../a)[%s]" % (block, type_index + 1)
        click_on("Тип: " + text, By.XPATH, choose_type)
        if self.counter == 0:
            self.ticket.get_info.append(text)
        else:
            self.ticket.get_round_info.append(text)

    def get_random_place(self):
        """ Gets available free place in chosen train and place category."""
        free_places = "//*[contains(@class,'sits_block')]//a"
        wait_list_elements("'Free places'", By.XPATH, free_places, 15)
        places = get_elements(By.XPATH, free_places)
        place_index = random.randint(0, places.__len__() - 1)
        text = element_text_content(places[place_index])
        place = "(%s)[%s]" % (free_places, place_index + 1)
        click_on("Место: " + text, By.XPATH, place)
        if self.counter == 0:
            self.ticket.get_info.append(text)
        else:
            self.ticket.get_round_info.append(text)

    def fill_passenger_form(self):
        last_name = "//*[contains(@id,'lastname')]"
        input_keys("Фамилия", By.XPATH, last_name, self.passenger.last_name)
        first_name = "//*[contains(@id,'firstname')]"
        input_keys("Имя", By.XPATH, first_name, self.passenger.first_name)
        full_name = self.passenger.last_name + " " + self.passenger.first_name
        self.ticket.get_info.append(full_name)
        self.ticket.get_round_info.append(full_name)

    def fill_contact_info(self):
        email = "//*[@id='user_form']//*[@id='email']"
        input_keys("Email", By.XPATH, email, self.passenger.email)
        phone = "//*[@id='buyer_data']//*[@id='phone_number']"
        input_keys("Номер телефона", By.XPATH, phone, self.passenger.phone)

    def accept_offerta(self):
        offerta = "//*[@id='i_accept_offerta']/.."
        click_on("Я принимаю правила публичной оферты", By.XPATH, offerta)

    def submit(self):
        price_locator = "//*[contains(@class,'buy-block')]//strong[not(contains(@class,'old-price'))]"
        price = element_text_content(get_element(By.XPATH, price_locator))
        if self.counter == 0:
            self.ticket.price = int(clear_price(price))
        else:
            self.ticket.round_price = int(clear_price(price))
        # Mark that one ticket is bought for writing info to round ticket
        self.counter = 1
        current_url = get_url()
        info("-----------------------------------")
        submit = "//*[contains(@class,'buy-block')]//*[@type='submit']"
        click_on("Продолжить", By.XPATH, submit)
        wait_change_url(current_url, 30)
