import logging

import pytest


def __log():
    f_o_r_m_a_t = "%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s"
    logging.basicConfig(format=f_o_r_m_a_t, datefmt='%H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger


@pytest.allure.step('{0}')
def info_test(message):
    __log().info(message)


@pytest.allure.step('{0}')
def warn(message):
    __log().warn(message)


@pytest.allure.step('{0}')
def error(message):
    __log().error(message)
