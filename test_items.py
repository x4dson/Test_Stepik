import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Визуально проверить кнопку на нужном языке
    add_to_cart_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_btn is not None, "Add to cart button is not present on the page"