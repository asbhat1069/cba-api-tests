import logging as logger
import requests
from constants import DEFAULT_API_TIMEOUT

default_timeout = DEFAULT_API_TIMEOUT
logger.basicConfig(level=logger.INFO)


class RESTClient:
    def __init__(self):
        self.user_session = requests

    def get(self, url, headers=None, timeout=default_timeout):
        logger.info("GET {}".format(url))
        logger.info("GET Headers: {}".format(headers))
        res = self.user_session.get(url, headers=headers, timeout=timeout)
        logger.info("Response Status Code : {}".format(res.status_code))
        logger.info("Response : {}".format(res.json()))
        res.raise_for_status()
        return res

    def post(
        self,
        url,
        payload=None,
        headers=None,
        timeout=default_timeout,
    ):
        logger.info("POST {}".format(url))
        logger.info("POST Headers: {}".format(headers))
        logger.info("POST Payload: {}".format(payload))
        res = self.user_session.post(
            url, json=payload, headers=headers, timeout=timeout
        )
        logger.info("Response Status Code : {}".format(res.status_code))
        if res.status_code != 204 and res.text:
            try:
                logger.info("Response : {}".format(res.json()))
            except ValueError:
                logger.info("Response : \n{}".format(res.text))
        res.raise_for_status()
        return res

    def put(self, url, payload, headers=None, timeout=default_timeout):
        logger.info("PUT {}".format(url))
        logger.info("PUT Headers: {}".format(headers))
        logger.info("PUT Payload: {}".format(payload))
        res = self.user_session.put(url, json=payload, headers=headers, timeout=timeout)
        logger.info("Response Status Code : {}".format(res.status_code))
        res.raise_for_status()
        return res

    def delete(self, url, headers=None, timeout=default_timeout):
        logger.info("DELETE {}".format(url))
        res = self.user_session.delete(url, headers=headers, timeout=timeout)
        logger.info("Response Status Code : {}".format(res.status_code))
        res.raise_for_status()
        return res

