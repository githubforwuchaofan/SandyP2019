# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午5:52
_desc: //ToDo
"""

import json
import logging
import re
import time

import requests
from requests import Request, Response
from requests.exceptions import (InvalidSchema, InvalidURL, MissingSchema,
                                 RequestException)

absolute_http_url_regexp = re.compile(r"^https?://", re.I)


def prepare_kwargs(method, kwargs):
    if method == "POST":
        content_type = kwargs.get("headers", {}).get("content-type", "")
        if content_type.startswith("application/json") and "data" in kwargs:
            kwargs["data"] = json.dumps(kwargs["data"])


class ApiResponse(Response):
    def raise_for_status(self):
        if hasattr(self, 'error') and self.error:
            raise self.error
        Response.raise_for_status(self)


class HttpSession(requests.Session):

    def __init__(self, base_url=None):
        super(HttpSession, self).__init__()
        self.base_url = base_url if base_url else ""

    def _build_url(self, path):
        """ prepend url with hostname unless it's already an absolute URL """
        if absolute_http_url_regexp.match(path):
            return path
        elif self.base_url:
            return "%s%s" % (self.base_url, path)
        else:
            raise ParamsError("base url missed!")

    def request(self, method, url, name=None, **kwargs):
        url = self._build_url(url)
        logging.info(" Start to {method} {url}".format(method=method, url=url))
        logging.debug(" kwargs: {kwargs}".format(kwargs=kwargs))
        request_meta = {"method": method, "start_time": time.time()}

        if "httpntlmauth" in kwargs:
            from requests_ntlm import HttpNtlmAuth
            auth_account = kwargs.pop("httpntlmauth")
            kwargs["auth"] = HttpNtlmAuth(
                auth_account["username"], auth_account["password"])

        response = self._send_request_safe_mode(method, url, **kwargs)
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

        logging.debug(" response: {response}".format(response=request_meta))

        try:
            response.raise_for_status()
        except RequestException as e:
            logging.error(" Failed to {method} {url}! exception msg: {exception}".format(
                method=method, url=url, exception=str(e)))
        else:
            logging.info(
                """ status_code: {}, response_time: {} ms, response_length: {} bytes""".format(
                    request_meta["status_code"], request_meta["response_time"], request_meta["content_size"]))

        return response

    def _send_request_safe_mode(self, method, url, **kwargs):
        try:
            prepare_kwargs(method, kwargs)
            return requests.Session.request(self, method, url, **kwargs)
        except (MissingSchema, InvalidSchema, InvalidURL):
            raise
        except RequestException as ex:
            resp = ApiResponse()
            resp.error = ex
            resp.status_code = 0  # with this status_code, content returns None
            resp.request = Request(method, url).prepare()
            return resp


