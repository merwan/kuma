# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.home import HomePage

# header tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_header_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Header.is_displayed

#footer tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_footer_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Footer.is_displayed

@pytest.mark.smoke
@pytest.mark.nondestructive
def test_select_language_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Footer.select_language_is_displayed

@pytest.mark.smoke
@pytest.mark.nondestructive
def test_select_language_is_locale_match(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Footer.select_language_is_locale_match

#homepage tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_masthead_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.is_masthead_displayed


