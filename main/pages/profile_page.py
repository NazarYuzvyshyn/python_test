from main.custom_utils.web_driver_factory import WebDriverFactory
from main.custom_utils.web_elem_servise import element_text_content


class ProfilePage:
    driver = WebDriverFactory.driver()

    email = "//*[@for='reg_email']/../following-sibling::*[contains(@class,'field')]/b"

    def user_email(self):
        return element_text_content(self.email)


