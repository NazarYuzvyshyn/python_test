import logging
import os

import pytest


@pytest.fixture(scope="function")
def fixer():
    print("Hello,i'm fixer")
    return fixer


@pytest.fixture(scope="function")
def mikser():
   print("Hi,i'm mikser")
   return mikser


# @pytest.fixture(scope='function')
# def modlog(request):
#     """Logger that also writes to a file."""
#     name = request.module.__name__
#     if name.startswith('test_'):
#         name = name[5:]
#     logname = 'TEST-' + name + '.log'
#     logger = logging.getLogger('simple_example')
#     logger.setLevel(logging.DEBUG)
#
#     # создаём консольный handler и задаём уровень
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.DEBUG)
#
#     # создаём formatter
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#     # добавляем formatter в ch
#     ch.setFormatter(formatter)
#
#     # добавляем ch к logger
#     logger.addHandler(ch)
#     return logger
