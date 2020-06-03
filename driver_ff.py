# Copyright (C) 2020 Robert-Nicolae Șolcă
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class DriverFirefox:
    def __init__(self, headless=False):
        self.headless = headless
        options = Options()
        options.set_preference("browser.link.open_newwindow", 1)
        profile = webdriver.FirefoxProfile()
        options.headless = headless
        self.driver = webdriver.Firefox(
            options=options, firefox_profile=profile)

    def goto(self, site):
        self.driver.get(site)

    def click(self, xpath):
        elem = self._find(xpath)
        elem.click()

    def send_keys(self, xpath, keys):
        elem = self._find(xpath)
        elem.send_keys(keys)

    def get_value(self, xpath, attribute):
        elem = self._find(xpath)
        return elem.get_attribute(attribute)

    def is_selected(self, xpath):
        elem = self._find(xpath)
        return elem.is_selected()

    def refresh(self):
        self.driver.refresh()

    def _find(self, xpath):
        return self.driver.find_element_by_xpath(xpath)
