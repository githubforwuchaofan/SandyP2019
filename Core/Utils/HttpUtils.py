# coding=utf8

"""
_author: wcf
_date: 2018/12/12-下午6:54
_desc: //ToDo
"""
import time
import requests
from requests import RequestException

from Core.Utils.LogUtils import LogUtils

logUtils = LogUtils()


class HttpUtils(object):
    @classmethod
    def send(cls, url, json=None, method='POST', **kwargs):
        logUtils.info(" Start to {method} {url}".format(method=method, url=url))
        logUtils.debug("data:{0}\nkwargs: {1}".format(json, kwargs))
        request_meta = {"method": method, "start_time": time.time()}

        response = requests.request(method, url, **kwargs)
        request_meta["url"] = (response.history and response.history[0] or response) \
            .request.path_url

        request_meta["response_time"] = int((time.time() - request_meta["start_time"]) * 1000)

        if kwargs.get("stream", False):
            request_meta["content_size"] = int(response.headers.get("content-length") or 0)
        else:
            request_meta["content_size"] = len(response.content or "")

        request_meta["request_headers"] = response.request.headers
        request_meta["request_body"] = response.request.body
        request_meta["status_code"] = response.status_code
        request_meta["response_headers"] = response.headers
        request_meta["response_content"] = response.content

        logUtils.debug(" response: {response}".format(response=request_meta))

        try:
            response.raise_for_status()
        except RequestException as e:
            logUtils.error(" Failed to {method} {url}! exception msg: {exception}".format(
                method=method, url=url, exception=str(e)))
        else:
            logUtils.info(
                """ status_code: {}, response_time: {} ms, response_length: {} bytes""".format(
                    request_meta["status_code"], request_meta["response_time"], request_meta["content_size"]))

        return response

