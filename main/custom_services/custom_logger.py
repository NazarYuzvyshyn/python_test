import logging

import allure


def __log():
    f_o_r_m_a_t = "%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s"
    logging.basicConfig(format=f_o_r_m_a_t, datefmt='%H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger


@allure.step('massage={0}')
def info(message):
    __log().info(message)


@allure.step('massage={0}')
def warn(message):
    __log().warn(message)


@allure.step('massage={0}')
def error(message):
    __log().error(message)
