from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://example.com/python'
driver = webdriver.Chrome()

driver.get(url)

jobs = driver.find_elements_by_class_name('job')

for job in jobs:
	title = job.find_element_by_tag_name('h2').text
	company = job.find_element_by_class_name('company').text
	location = job.find_element_by_class_name('location').text

	if location == 'Tokyo':
		apply_button = job.find_element_by_class_name('apply')
		apply_button.click()

		# 応募フォームの操作
		name_input = driver.find_element_by_name('name')
		name_input.send_keys('山田太郎')

		email_input = driver.find_element_by_name('email')
		email_input.send_keys('yamada@example.com')

		submit_button = driver.find_element_by_class_name('submit')
		submit_button.click()
