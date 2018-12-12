# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午1:41
_desc: //ToDo
"""
import requests

from Core.sExceptions.BaseExceptions import BaseExceptions


class MissingSchemaError(BaseExceptions):
    pass


class HttpConnectError(BaseExceptions):
    pass


class HttpParameterError(BaseExceptions):
    pass


if __name__ == '__main__':
    try:
        requests.post(url='www.baidu.com')
    except Exception as err:
        MissingSchemaError(err)

    try:
        requests.post(url='http://www.sandy.com', timeout=5)
    except requests.ConnectTimeout as err:
        HttpConnectError(err)

