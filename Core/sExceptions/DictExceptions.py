# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午1:46
_desc: //ToDo
"""
from Core.sExceptions.BaseExceptions import BaseExceptions


class KeyNotFoundError(BaseExceptions):
    pass


class JsonFormatError(BaseExceptions):
    pass


class DictIsEmptyError(BaseExceptions):
    pass


if __name__ == '__main__':
   dict_1 = {'name': 'sandy', 'age': 27}
   try:
       age = dict_1['sex']
   except Exception as err:
       KeyNotFoundError(err)

