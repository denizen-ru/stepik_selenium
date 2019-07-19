from selenium import webdriver


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

number1 = int(browser.find_element_by_id('num1').text)
number2 = int(browser.find_element_by_id('num2').text)
result = number1 + number2

browser.find_element_by_id("dropdown").click()
browser.find_element_by_css_selector("[value='{}']".format(result)).click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
