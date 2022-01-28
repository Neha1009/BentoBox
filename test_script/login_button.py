from selenium import webdriver
from time import sleep


def test_faq_text():
    driver = webdriver.Chrome(r"C:\Users\panka\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('http://localhost/BentoBox-1/')
    sleep(3)
    order_now_xpath = '//a[text()="Order Now"]'
    order_now_text = 'ORDER NOW'
    order_now_menu = driver.find_element_by_xpath(order_now_xpath)
    assert order_now_text == order_now_menu.text, "text not matching"
    print('expected text is matching')
    order_now_menu.click()
    print('Opening order now page...')
    login_xpath = "(//a[text()='Login'])[2]"
    sleep(3)
    login_button = driver.find_element_by_xpath(login_xpath)
    login_button_text = 'Login'
    assert login_button_text == login_button.text
    login_button.click()
    print('Opening login page...')

    sleep(3)
    driver.close()
