from pages.base_page import BasePage
from pages.components.canvas_component import CanvasComponent
from pages.components.header_menu_component import HeaderMenuComponent


class HomePage(BasePage):
    header_menu_component: HeaderMenuComponent = None
    canvas_component: CanvasComponent = None

    def __init__(self, driver):
        super().__init__(driver)
        self.header_menu_component = HeaderMenuComponent(driver)
        self.canvas_component = CanvasComponent(driver)

    def verify_header_elements(self):
        self.header_menu_component.verify_page_elements()

    def verify_canvas_elements(self):
        self.canvas_component.verify_page_elements()
