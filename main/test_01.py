# -*- coding: utf-8 -*-
import pytest
import sys
import allure
sys.path.append('..')
from case.theme import theme


@allure.feature('login')
def test_1():
    roleinfos=theme().login()
    assert roleinfos == u"区域用户"

    
   
