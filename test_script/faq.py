from selenium import webdriver
from time import sleep


def test_faq_text():
    driver = webdriver.Chrome(r"C:\Users\panka\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('http://localhost/BentoBox-1/')
    sleep(3)
    faq_xpath = '//a[text()="FAQ"]'
    faq_text = 'FAQ'
    faq_menu = driver.find_element_by_xpath(faq_xpath)
    assert faq_text == faq_menu.text, "text not matching"
    print('expected text is matching')
    faq_menu.click()
    print('Opening faq page...')

    sleep(3)
    driver.close()
