# coding=utf8

"""
_author: wcf
_date: 2018/12/13-下午8:41
_desc: //ToDo
"""
import importlib


class ModuleUtils(object):

    @staticmethod
    def get_imported_module(module_name):
        """ import module and return imported module
        """
        return importlib.import_module(module_name)

    @staticmethod
    def is_function(func):
        return isinstance(func, function)

    @staticmethod
    def is_module():
        return isinstance()
