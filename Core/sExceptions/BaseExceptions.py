# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午1:50
_desc: //ToDo
"""


from Core.Utils.LogUtils import LogUtils

logUtils = LogUtils()


class BaseExceptions(Exception):
    global logUtils

    def __init__(self, _exc, *args, **kwargs):
        self.exc = _exc
        self.args = args
        self.kwargs = kwargs
        self._exc()

    def _exc(self):
        if isinstance(self.exc, Exception):
            logUtils.exception(self.exc)
        else:
            logUtils.error(self.exc)

        self.args and [logUtils.info(arg) for arg in self.args]
        self.kwargs and logUtils.info(self.kwargs)