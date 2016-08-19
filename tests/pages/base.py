# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pypom import Page, Region

class BasePage(Page):

    URL_TEMPLATE = '/{locale}'

    def __init__(self, selenium, base_url, locale='en-US', **url_kwargs):
        super(BasePage, self).__init__(selenium, base_url, locale=locale, **url_kwargs)

    @property
    def header(self):
        return self.Header(self)

    @property
    def footer(self):
        return self.Footer(self)

    class Header(Region):
        _root_locator = (By.ID, 'main-header')
        _menu_locator = (By.ID, 'nav-main-menu')

        # is displayed?
        @property
        def is_displayed(self):
            return self.root.is_displayed()

    class Footer(Region):
        _root_locator = (By.ID, 'main-footer')
        _language_locator = (By.ID, 'language')
        _privacy_locator = (By.CLASS_NAME, '.contentinfo')
        _license_locator = (By.CLASS_NAME, '.contentinfo')

        # is displayed?
        @property
        def is_displayed(self):
            return self.root.is_displayed()

        # language drop down
        def select_language(self):
            return self.find_element(*self._language_locator)

        #language select is displayed
        @property
        def select_language_is_displayed(self):
            return self.select_language.is_displayed()

        # check lanuage selected in drop down matches locale
        @property
        def select_language_is_locale_match(self, locale):
            #get language selected
            select_language.find_element(option[selected]).get_attribute('value')
            return (language_selected == locale)


        # check changing language works

        """
        @property
        def language(self):
            select = self.find_element(*self._language_locator)
            option = select.find_element(By.CSS_SELECTOR, 'option[selected]')
            return option.get_attribute('value')

        @property
        def languages(self):
            el = self.find_element(*self._language_locator)
            return [o.get_attribute('value') for o in Select(el).options]

        def select_language(self, value):
            el = self.find_element(*self._language_locator)
            Select(el).select_by_value(value)
            self.wait.until(lambda s: '/{0}/'.format(value) in s.current_url)
"""
