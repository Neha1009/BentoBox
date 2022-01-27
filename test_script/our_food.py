from selenium import webdriver
from time import sleep


def test_our_food_text():
    try:
        driver = webdriver.Chrome(r"C:\Users\panka\Downloads\chromedriver_win32\chromedriver.exe")
        driver.get('http://localhost/BentoBox-1/')
        sleep(3)
        our_food_xpath = '//a[text()="Our Food"]'
        our_food_text = 'OUR FOOD'
        our_food_menu = driver.find_element_by_xpath(our_food_xpath)
        assert our_food_text == our_food_menu.text, "text not matching"
        print('expected text is matching')
        our_food_menu.click()
        print('Opening our food page...')
        sleep(5)

    finally:
        driver.close()
