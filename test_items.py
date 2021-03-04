"""
pytest -s -v --tb=short --browser_name=chrome --language=es test_items.py
pytest -s -v --language=es
ВНИМАНИЕ:  time.sleep(30) добавляет проверяющий самостоятельно!
"""

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_busket_presents_in_site(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button.is_displayed(), "Button add to basket not displayed."