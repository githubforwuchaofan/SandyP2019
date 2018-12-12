# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午6:58
_desc: //ToDo
"""
import logging

from ddt import ddt, file_data
import unittest


def plus(x, y):
    logging.error(str(x + y))
    return x, y


@ddt
class TestDDT(unittest.TestCase):
    @file_data('./DdtTestData.json')
    def test_add(self, x, y, z):
        logging.info('{0}{1}{2}'.format(x, y, z))
        assert x + y == z
        plus(x, y)

if __name__ == '__main__':
    import os

    os.system('pytest DdtTest.py --html=./report/report.html -o log_cli=true -o log_cli_level=ERROR')
