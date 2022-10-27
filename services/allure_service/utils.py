import base64
import os
import sys

from globals import dir_global
from services.allure_service.model import PostSendResultRequest, ResultRequestFile


def get_json_result_request_files_by_path(path_to_directory):
    post_send_result_request = PostSendResultRequest()
    post_send_result_request.results = []
    try:
        for filename in os.listdir(dir_global.ALLURE_RESULTS_PATH):
            f = os.path.join(dir_global.ALLURE_RESULTS_PATH, filename)
            if os.path.isfile(f) \
                    and filename.__contains__(".json") \
                    or filename.__contains__(".attach"):
                file = open(f, 'r')
                content = base64.b64encode(file.read().encode())
                post_send_result_request.results.append(
                    ResultRequestFile(content_base64=content.decode(), file_name=filename))
    except FileNotFoundError as e:
        print(f"Unable to open {path_to_directory}: {e}", file=sys.stderr)
        return

    return post_send_result_request.json


def clean_all_files_from_directory():
    for filename in os.listdir(dir_global.ALLURE_RESULTS_PATH):
        f = os.path.join(dir_global.ALLURE_RESULTS_PATH, filename)
        os.remove(f)
