import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element_by_name('firstname')
firstname.send_keys('Karl')

lastname = browser.find_element_by_name('lastname')
lastname.send_keys('Marx')

email = browser.find_element_by_name('email')
email.send_keys('karl.marx@gov.de')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
upload = browser.find_element_by_id('file')
upload.send_keys(file_path)

browser.find_element_by_css_selector("button.btn").click()
