from services.allure_service.controller import InfoController, SecurityController, ProjectController, ActionController


class AllureService:
    def __init__(self):
        self.info = InfoController()
        self.security = SecurityController()
        self.project = ProjectController()
        self.action = ActionController()
