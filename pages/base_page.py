from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 15)

    def _go_to_page(self, url):
        self._driver.get(url)

    def get_title(self):
        return self._driver.title

    def _click(self, web_element):
        element = self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        element.click()

    def _move_to_element(self, web_element):
        action = ActionChains(self._driver)
        self._wait.until(expected_conditions.visibility_of(web_element))
        action.move_to_element(web_element).perform()

    def _fill_text(self, web_element, txt):
        el = self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        el.clear()
        el.send_keys(txt)

    def _find_elements(self, web_element):
        self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        return self._driver.find_elements(*web_element)

    def _is_elem_displayed(self, web_element, timeout=10):
        try:
            element = WebDriverWait(self._driver, timeout) \
                .until(expected_conditions.element_to_be_clickable(web_element))
            return element.is_displayed()
        except TimeoutException:
            return False
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False
