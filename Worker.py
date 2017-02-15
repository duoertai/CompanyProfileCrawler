from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from Queue import Queue
from pyvirtualdisplay import Display
from sets import Set

import re
import threading


class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.driver = webdriver.Chrome()
        self.queue = queue

    def work(self, url):
        self.driver.get(url)

        # get company name
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']"))
        WebDriverWait(self.driver, 30).until(element_present)
        company_name = self.driver.find_element_by_xpath(
            "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/h3[@class='Mb(10px)']")
        company_name = str(company_name.text)

