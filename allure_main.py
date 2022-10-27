import sys

from services.allure_service.allure_service import AllureService

allure_service = AllureService()


def reg_project(project_id):
    allure_service.action.get_clean_results(project_id=project_id)


def gen_results(project_id):
    allure_service.action.post_send_results(project_id=project_id, force_project_creation=True)
    allure_service.action.get_generate_report(project_id=project_id)


if __name__ == "__main__":
    globals()[sys.argv[1]](sys.argv[2])
