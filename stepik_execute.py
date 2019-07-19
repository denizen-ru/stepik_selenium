from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

browser.execute_script("window.scrollBy(0, 100);")

text_field = browser.find_element_by_id("answer")
text_field.send_keys(calc(browser.find_element_by_id('input_value').text))

browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
