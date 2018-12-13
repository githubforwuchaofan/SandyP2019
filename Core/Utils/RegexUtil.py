# coding=utf8

"""
_author: wcf
_date: 2018/12/12-下午6:22
_desc: //ToDo
"""
import re

from Core.Utils.LogUtils import LogUtils

logUtils = LogUtils()


class RegexUtil(object):
    def __init__(self, _pattern, _text, _repl=None):
        self._pattern = re.compile(_pattern)
        self._text = _text
        self._repl = _repl
        logUtils.info('pattern={0}\n\ttext={1}\n\trepl={2}'.format(self._pattern, self._text, self._repl))

    def match(self):
        return re.match(pattern=self._pattern, string=self._text)

    def search(self):
        return re.search(pattern=self._pattern, string=self._text)

    def sub(self):
        return re.sub(self._pattern, repl=self._repl, string=self._text)

    def find_all(self):
        return re.findall(self._pattern, self._text)


if __name__ == '__main__':
    text = '123456789ABCDEFGabcdefg'
    pattern = '\w'
    repl = '00'
    r = RegexUtil(pattern, text, repl)
    print(r.match() and True or False)
    print(r.search() and True or False)
    print(r.sub())
    print(r.find_all())
