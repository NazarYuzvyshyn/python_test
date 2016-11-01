import platform

import pytest

from main.custom_utils.custom_logger import log
from tests.test_Pop.conftest import fixer, mikser

s = "mu"
luka = [["atom", "botom"], ["kot", "pot"]]



@pytest.mark.parametrize("bomba", luka)
def test_pest(bomba,request):

    log().info("insert " + bomba[0] + "||" + bomba[1])
    log().error("what are fuck")




def test_tust():

    print("======= test trust =============")
