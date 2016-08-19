# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypom import Region
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected

from pages.base import BasePage


class HomePage(BasePage):

    _masthead_locator = (By.CSS_SELECTOR, '.home-masthead')

    @property
    def is_masthead_displayed(self):
        return self.find_element(*self._masthead_locator).is_displayed()
