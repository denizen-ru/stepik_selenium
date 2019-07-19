from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

text_field = browser.find_element_by_id("answer")
text_field.send_keys(calc(browser.find_element_by_id('input_value').text))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_css_selector("[value='robots']")
radio.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
