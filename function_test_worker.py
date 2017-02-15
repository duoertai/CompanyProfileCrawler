from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from Queue import Queue
from pyvirtualdisplay import Display
from sets import Set
import string


driver = webdriver.Chrome()
driver.get("http://finance.yahoo.com/quote/INTC/profile?p=INTC")

element_present = EC.presence_of_element_located((By.XPATH,
                                                          "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/section[@id='quote-nav']/ul[@class='Lh(1.7) List(n) P(0) Whs(nw) H(50px) Bdbs(s) BdB(4px) Bdbc($lightGray) Cf']/li[@class='Fl(start) H(50px) Fw(500) Bgc($lightBlue):h quote-nav-collapse-list_W(100%) quote-nav-collapse-list_H(45px) quote-nav-item Selected ']/a[@class='D(b) Td(n) Lh(50px) quote-nav-collapse-list_Lh(45px) Ta(c) quote-nav-collapse-list_Ta(start) Bdbw(3px) Bdbs(s) Bdbc(t) Px(15px) quote-nav-collapse-list_Pend(0) Selected_Bdbc($brandBlue) Selected_C($finDarkLink) Selected_Bgc($navSelectedBlue) active']/span"))
WebDriverWait(driver, 30).until(element_present)

'''
profile_button = driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/section[@id='quote-nav']/ul[@class='Lh(1.7) List(n) P(0) Whs(nw) H(50px) Bdbs(s) BdB(4px) Bdbc($lightGray) Cf']/li[@class='Fl(start) H(50px) Fw(500) Bgc($lightBlue):h quote-nav-collapse-list_W(100%) quote-nav-collapse-list_H(45px) quote-nav-item Selected ']/a[@class='D(b) Td(n) Lh(50px) quote-nav-collapse-list_Lh(45px) Ta(c) quote-nav-collapse-list_Ta(start) Bdbw(3px) Bdbs(s) Bdbc(t) Px(15px) quote-nav-collapse-list_Pend(0) Selected_Bdbc($brandBlue) Selected_C($finDarkLink) Selected_Bgc($navSelectedBlue) active']")
profile_button.click()
'''

element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']"))
WebDriverWait(driver, 30).until(element_present)
company_name = driver.find_element_by_xpath(
    "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/h3[@class='Mb(10px)']")
print str(company_name.text)

info = driver.find_element_by_xpath(
    "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) W(47.727%) Pend(40px)']")


element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) W(47.727%) Pend(40px)']"))
WebDriverWait(driver, 30).until(element_present)
info = driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) W(47.727%) Pend(40px)']")
print info.text

lines = string.split(str(info.text), '\n')
print lines

element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[1]"))
WebDriverWait(driver, 30).until(element_present)
sector = driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[1]")
print sector.text

element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[2]"))
WebDriverWait(driver, 30).until(element_present)
industry = driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[2]")
print industry.text

element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[3]/span"))
WebDriverWait(driver, 30).until(element_present)
full_time_employee = driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-Quote-Proxy']/section[@class='Pos(r) Z(1)']/div[@class='W(100%) Pos(r)']/section[@class='Va(t) Mend(340px) Mend(0)!--tab768']/div[@class='Pb(30px)']/div[@class='asset-profile-container']/div[@class='qsp-2col-profile Mt(15px) Lh(1.7)']/div[@class='Mb(35px)']/p[@class='D(ib) Va(t)']/strong[3]/span")
print full_time_employee.text

driver.quit()