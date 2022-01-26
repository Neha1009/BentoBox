from selenium import webdriver
from time import sleep


def test_order_now_text():
    try:
        driver = webdriver.Chrome(r"C:\Users\panka\Downloads\chromedriver_win32\chromedriver.exe")
        driver.get('http://localhost/BentoBox/')
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
        driver.find_element_by_name('username').send_keys('user2')
        driver.find_element_by_name('password').send_keys('pass2')
        sleep(3)
        login_xpath = "//a[text()='Login']"
        login_button = driver.find_element_by_xpath(login_xpath)
        login_button.click()

        sleep(6)

    finally:
        driver.close()
