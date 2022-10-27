import logging
import sys

import requests
from tenacity import retry, wait_fixed, stop_after_attempt, retry_if_result

from services.allure_service.abstract_controller import AbstractController
from services.allure_service.http_formatter import HttpFormatter, logRoundtrip
from services.allure_service.retry import is_bad_request
from services.allure_service.utils import get_json_result_request_files_by_path, clean_all_files_from_directory

root = logging.getLogger('httplogger')

formatter = HttpFormatter('{asctime} {levelname} {name} {message}', style='{')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
root.addHandler(handler)
root.setLevel(logging.DEBUG)

session = requests.Session()
session.hooks['response'].append(logRoundtrip)


def _get_params(session):
    # return {"x-csrf-token": session.cookies['csrf_access_token']}
    return {"x-csrf-token": ''}


class InfoController(AbstractController):

    def get_swagger(self) -> requests.Response:
        return session.get(f"{self.host}/swagger")

    def get_swagger_json(self) -> requests.Response:
        return session.get(f"{self.host}/swagger.json")

    def get_version(self) -> requests.Response:
        return session.get(f"{self.host}/version")


class SecurityController(AbstractController):

    def post_login(self, username: str, password: str) -> requests.Response:
        return session.post(url=f"{self.host}/login", json={'username': username, 'password': password})

    def delete_logout(self) -> requests.Response:
        return session.delete(url=f"{self.host}/logout", headers=_get_params(session))

    def delete_logout_refresh_token(self) -> requests.Response:
        return session.delete(url=f"{self.host}/logout-refresh-token", headers=_get_params(session))

    def post_refresh(self) -> requests.Response:
        return session.post(url=f"{self.host}/refresh", headers=_get_params(session))


class ActionController(AbstractController):

    def get_clean_history(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/clean-history", params={"project_id": project_id})

    def get_clean_results(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/clean-results", params={"project_id": project_id})

    def get_config(self) -> requests.Response:
        return session.get(f"{self.host}/config")

    def get_emailable_report_export(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/emailable-report/export", params={"project_id": project_id})

    def get_emailable_report_render(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/emailable-report/render", params={"project_id": project_id})

    @retry(wait=wait_fixed(5), stop=stop_after_attempt(3), retry=retry_if_result(is_bad_request))
    def get_generate_report(self, project_id,
                            execution_name=None,
                            execution_from=None,
                            execution_type=None) -> requests.Response:
        rs = session.get(f"{self.host}/generate-report", params={"project_id": project_id,
                                                                   "execution_name": execution_name,
                                                                   "execution_from": execution_from,
                                                                   "execution_type": execution_type})
        clean_all_files_from_directory()
        return rs

    def get_latest_report(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/latest-report", params={"project_id": project_id})

    def get_report_export(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/report/export", params={"project_id": project_id})

    def post_send_results(self, project_id: str,
                          force_project_creation: bool = False,
                          path_to_files: str = "allure-results") -> requests.Response:
        headers = _get_params(session)
        headers["content-type"] = "application/json"
        response = session.post(f"{self.host}/send-results",
                                data=get_json_result_request_files_by_path(path_to_files),
                                headers=headers,
                                params={"project_id": project_id,
                                        "force_project_creation": str(force_project_creation).lower()})
        return response


class ProjectController(AbstractController):

    def get_projects(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/projects", json={f"id": project_id})

    def post_project(self) -> requests.Response:
        return session.post(f"{self.host}/projects", headers=_get_params(session))

    def get_project_search(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/project/search", params={"id": project_id})

    def delete_project(self, project_id) -> requests.Response:
        return session.delete(f"{self.host}/project/search", headers=_get_params(session), params={"id": project_id})

    def get_project(self, project_id) -> requests.Response:
        return session.get(f"{self.host}/projects/{project_id}", params={"id": project_id})

    def get_project_report(self, project_id, path="allure/reports", redirect=False) -> requests.Response:
        return session.get(f"{self.host}/projects/{id}/reports/{path}", params={"id": project_id,
                                                                                "path": path,
                                                                                "redirect": redirect})
