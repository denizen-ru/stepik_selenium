from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector("button.trollface").click()

browser.switch_to.window(browser.window_handles[1])

text_field = browser.find_element_by_id("answer")
text_field.send_keys(calc(browser.find_element_by_id('input_value').text))

browser.find_element_by_css_selector("button.btn").click()
