import logging
import pytest


def __log():
    f_o_r_m_a_t = "%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s"
    logging.basicConfig(format=f_o_r_m_a_t, datefmt='%H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger


@pytest.allure.step('{message}')
def info(message):
    __log().info(message)


@pytest.allure.step('{message}')
def warn(message):
    __log().warn(message)


@pytest.allure.step('{message}')
def error(message):
    __log().error(message)
