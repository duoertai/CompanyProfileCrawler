from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
browser = webdriver.Chrome()
browser.get('http://google.com')
'''

driver = webdriver.PhantomJS()
driver.get('http://www.python.org')
assert 'Python' in driver.title
element = driver.find_element_by_name('q')
element.send_keys('pycon')
element.send_keys(Keys.RETURN)
print driver.page_source
