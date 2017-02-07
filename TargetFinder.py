from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading

class TargetFinder(threading.Thread):
    def __init__(self):
        pass


driver = webdriver.Chrome()
driver.get('http://finance.yahoo.com/screener/new')
add_sector_button = driver.find_element_by_xpath("//div[@class='D(ib) Bgc(white) Bdrs(3px)']//div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f Cur(p)']")
add_sector_button.click()

technology_checkbox = driver.find_element_by_xpath("//div[@class='Pstart(16px) Pend(20px) Mah(230px) Ovy(a)']//li/label/span[contains(.., 'Technology')]")
technology_checkbox.click()