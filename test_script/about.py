from selenium import webdriver
from time import sleep


def test_about_text():
    driver = webdriver.Chrome(r"C:\Users\panka\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('http://localhost/BentoBox-1/')
    sleep(3)
    about_xpath = '//a[text()="About Us"]'
    about_text = 'ABOUT US'
    about_menu = driver.find_element_by_xpath(about_xpath)
    assert about_text == about_menu.text, "text not matching"
    print('expected text is matching')
    about_menu.click()
    print('Opening about page...')

    sleep(3)
    driver.close()


