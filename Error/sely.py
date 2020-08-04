from selenium import webdriver
chrome_browser = webdriver.Chrome('D:/Softwares/msvcp120/chromedriver_win32/chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('http://www.seleniumeasy.com/test/basic-first-form-demo.html')

#assert 'Selenium Easy - Best Demo website to practice Selenium Webdriver Online' in chrome_browser.title
assert 'Selenium Easy Demo' in chrome_browser.title
button=chrome_browser.find_element_by_class_name('btn-default')
print(button)
print(button.get_attribute('innerHTML'))

#####################LOGIN########################################################################
assert 'Show Message' in chrome_browser.page_source
user_message =chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOL')
button.click()
output_message=chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOL' in output_message.text

user_button=chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button)