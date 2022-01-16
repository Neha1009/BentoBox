from selenium import webdriver
from time import sleep


def test_faq_text():
    driver = webdriver.Chrome(r'C:\Users\Nikki\Downloads\chromedriver.exe')
    driver.get('http://localhost/devops/')
    faq_xpath = '//a[text()="FAQ"]'
    faq_text = 'FAQ'
    faq_menu = driver.find_element_by_xpath(faq_xpath)
    assert faq_text == faq_menu.text, "text not matching"
    print('expected text is matching')
    faq_menu.click()
    print('Opening faq page...')

    sleep(5)
    driver.close()
