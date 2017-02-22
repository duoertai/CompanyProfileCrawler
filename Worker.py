from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from Queue import Queue
from pyvirtualdisplay import Display
from sets import Set
import string
import re
import threading


class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
        self.queue = queue

    def work(self, url):
        self.driver.get(url)

        # get company name
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']"))
        try:
            WebDriverWait(self.driver, 10).until(element_present)
            company_name = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/h3[@class='Mb(10px)']")
            company_name = str(company_name.text)
        except:
            company_name = ""
        print company_name

        # get address, telephone, website url
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) W(47.727%) Pend(40px)']"))
        try:
            WebDriverWait(self.driver, 10).until(element_present)
            info = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) W(47.727%) Pend(40px)']")
            lines = string.split(str(info.text), '\n')
            address = lines[0]
            for i in range(1, len(lines) - 2):
                address = address + " " + lines[i]
            telephone = lines[len(lines) - 2]
            website_url = lines[len(lines) - 1]
        except:
            address = ""
            telephone = ""
            website_url = ""

        print address
        print telephone
        print website_url


        # get sector
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[1]"))
        try:
            WebDriverWait(self.driver, 10).until(element_present)
            sector = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[1]")
            sector = str(sector.text)
        except:
            sector = ""
        print sector

        # get industry
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[2]"))
        try:
            WebDriverWait(self.driver, 10).until(element_present)
            industry = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[2]")
            industry = str(industry.text)
        except:
            industry = ""
        print industry

        # get full time employee count
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[3]/span"))
        try:
            WebDriverWait(self.driver, 10).until(element_present)
            full_time_employee = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[3]/span")
            full_time_employee = str(full_time_employee.text)
        except:
            full_time_employee = ""
        print full_time_employee

        # get key executives
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/section[@class='Bxz(bb) quote-subsection']"))
        try:
            WebDriverWait(self.driver, 10).until(element_present)
            table = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/section[@class='Bxz(bb) quote-subsection']/table[@class='W(100%)']/tbody")
            rows = table.find_elements(By.TAG_NAME, "tr")

            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td")[0]
                print col.text
                col = row.find_elements(By.TAG_NAME, "td")[1]
                print col.text
                col = row.find_elements(By.TAG_NAME, "td")[2]
                print col.text
                col = row.find_elements(By.TAG_NAME, "td")[3]
                print col.text
                col = row.find_elements(By.TAG_NAME, "td")[4]
                print col.text

        except:
            pass

        # get description
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/section[@class='quote-sub-section Mt(30px)']/p[@class='Mt(15px) Lh(1.6)']"))
        try:
            WebDriverWait(self.driver, 10).until(element_present)
            description = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/section[@class='quote-sub-section Mt(30px)']/p[@class='Mt(15px) Lh(1.6)']")
            print description.text
        except:
            description = ""

        self.driver.quit()


w = Worker('a')
w.work("http://finance.yahoo.com/quote/IBM/profile?p=IBM")