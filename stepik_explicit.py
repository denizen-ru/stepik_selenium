from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR')
)

browser.find_element_by_id("book").click()

text_field = browser.find_element_by_id("answer")
text_field.send_keys(calc(browser.find_element_by_id('input_value').text))

browser.find_element_by_id("solve").click()
