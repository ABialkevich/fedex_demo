from http import HTTPStatus

import requests


def is_bad_request(values: requests.Response):
    return values.status_code in [HTTPStatus.BAD_REQUEST]
