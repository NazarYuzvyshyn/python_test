import logging

import pytest


def __log():
    f_o_r_m_a_t = "%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s"
    logging.basicConfig(format=f_o_r_m_a_t, datefmt='%H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger


def info(message):
    with pytest.allure.step(title=message):
        __log().info(message)


def warn(message):
    with pytest.allure.step("{}".format(message)):
        __log().warn(message)


def error(message):
    with pytest.allure.step("{}".format(message)):
        __log().error(message)
