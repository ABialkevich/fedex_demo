import os
import time
from distutils.util import strtobool

from _pytest.fixtures import fixture
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from helper_enums.browser_enum import Browser
from models.config import Config
from utils.yaml_parser import YamlParser


def pytest_addoption(parser):
    parser.addoption("--localrun", action="store", default='true', help='Base URL for the API tests')
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="https://www.fedex.com/en-gb/home.html")
    parser.addoption("--headless", action="store", default='false')
    parser.addoption("--language", action="store", default='ENG')


@fixture()
def create_driver(request):
    driver_caught = False
    while driver_caught:
        try:
            os.environ['no_proxy'] = '*'
            config = Config()
            # the following conditions are needed to support local tests run
            if strtobool(request.config.option.localrun) == 1:
                config = Config().parse_obj(YamlParser("config.yaml").read())
            else:
                for key in Config().dict():
                    setattr(config, key, getattr(request.config.option, key))

            options = ArgOptions()
            if config.headless:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')

            if strtobool(config.localrun) == 1:
                if config.browser == Browser.CHROME.value:
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.arguments.extend(options.arguments)
                    driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()),
                                              options=chrome_options)
                elif config.browser == Browser.FIREFOX.value:
                    ff_options = webdriver.FirefoxOptions()
                    ff_options.arguments.extend(options.arguments)
                    driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()),
                                               options=ff_options)
            else:
                driver = webdriver.Remote("http://selenium:4444", desired_capabilities=DesiredCapabilities.FIREFOX)

            driver.maximize_window()
            driver.get(config.url)
            driver_caught = True
        except:
            print("Error initialisation of driver..")
            time.sleep(10)

    yield driver, config

    if driver is not None:
        # driver.close()
        driver.quit()
