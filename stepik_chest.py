from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_id('treasure').get_attribute('valuex')
text_field = browser.find_element_by_id("answer")
text_field.send_keys(calc(treasure))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
