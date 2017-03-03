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


class TargetFinder(threading.Thread):
    def __init__(self, queue, mark):
        threading.Thread.__init__(self)
        #self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
        self.driver = webdriver.Chrome()
        self.queue = queue
        self.set = Set()
        self.mark = mark

    def prepare_starting_page(self):
        # open the finance screener page
        self.driver.get('http://finance.yahoo.com/screener/new')

        # click add sector, choose technology sector, and close
        self.select_sector()

        # choose semiconductor related industries, and close
        self.select_industry()

        # find the stocks
        self.find_stock()

    def enqueue_links(self):
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/div[2]/section[@id='screener-results']/div[@class='Pos(r)']/div/div[@class='W(100%) Mt(15px) Ta(end)']/button[@class='Va(m) H(20px) Bd(0) M(0) P(0) Fz(s) Pstart(6px) O(n):f Fw(500) C($actionBlue)']/span[@class='Va(m)']/span"))
        WebDriverWait(self.driver, 30).until(element_present)
        list = []
        set = Set()
        next_button = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/div[2]/section[@id='screener-results']/div[@class='Pos(r)']/div/div[@class='W(100%) Mt(15px) Ta(end)']/button[@class='Va(m) H(20px) Bd(0) M(0) P(0) Fz(s) Pstart(6px) O(n):f Fw(500) C($actionBlue)']/span[@class='Va(m)']/span")
        WebDriverWait(self.driver, 10).until(element_present)

        while element_present:
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            res = soup.findAll('a', href=re.compile('/quote/[A-Z]+\?p=[A-Z]+'), recursive=True)
            for item in res:
                if item['href'] not in set:
                    list.append(item['data-symbol'])
                    self.queue.put(str(item['data-symbol']))

            next_button = self.driver.find_element_by_xpath(
                "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/div[2]/section[@id='screener-results']/div[@class='Pos(r)']/div/div[@class='W(100%) Mt(15px) Ta(end)']/button[@class='Va(m) H(20px) Bd(0) M(0) P(0) Fz(s) Pstart(6px) O(n):f Fw(500) C($actionBlue)']/span[@class='Va(m)']/span")
            next_button.click()
            try:
                WebDriverWait(self.driver, 10).until(element_present)
            except:
                break

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        res = soup.findAll('a', href=re.compile('/quote/[A-Z]+\?p=[A-Z]+'), recursive=True)
        for item in res:
            list.append(item['data-symbol'])
            self.queue.put(str(item['data-symbol']))

        # set mark to true to notify worker thread
        self.mark.set()

        for item in list:
            print item

        print len(list)
        self.driver.quit()

    def select_sector(self):
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][1]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f Cur(p)']/span[@class='Va(m) Mstart(6px) Mend(4px)']/span/span"))
        WebDriverWait(self.driver, 30).until(element_present)
        add_sector_button = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][1]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f Cur(p)']/span[@class='Va(m) Mstart(6px) Mend(4px)']/span/span")
        add_sector_button.click()

        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][1]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/div[@class='Py(15px)']/div[@class='Pstart(16px) Pend(20px) Mah(230px) Ovy(a)']/ul[@class='M(0) P(0)']/li[@class='Fl(start) D(b) Mb(10px)'][8]/label[@class='Ta(c) Pos(r) Va(tb) Pend(10px)']"))
        WebDriverWait(self.driver, 30).until(element_present)
        technology_checkbox = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][1]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/div[@class='Py(15px)']/div[@class='Pstart(16px) Pend(20px) Mah(230px) Ovy(a)']/ul[@class='M(0) P(0)']/li[@class='Fl(start) D(b) Mb(10px)'][8]/label[@class='Ta(c) Pos(r) Va(tb) Pend(10px)']")
        technology_checkbox.click()

        sector_close_button = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][1]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/button[@class='Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close']")
        sector_close_button.click()

    def select_industry(self):
        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][2]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f Cur(p)']"))
        WebDriverWait(self.driver, 30).until(element_present)

        add_industry_button = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][2]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f Cur(p)']")
        add_industry_button.click()

        target_list = [
            # "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][2]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/div[@class='Py(15px)']/div[@class='Pstart(16px) Pend(20px) Mah(230px) Ovy(a)']/ul[@class='M(0) P(0)']/li[@class='Fl(start) D(b) Mb(10px)'][15]/label[@class='Ta(c) Pos(r) Va(tb) Pend(10px)']",
            # "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][2]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/div[@class='Py(15px)']/div[@class='Pstart(16px) Pend(20px) Mah(230px) Ovy(a)']/ul[@class='M(0) P(0)']/li[@class='Fl(start) D(b) Mb(10px)'][17]/label[@class='Ta(c) Pos(r) Va(tb) Pend(10px)']",
            # "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][2]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/div[@class='Py(15px)']/div[@class='Pstart(16px) Pend(20px) Mah(230px) Ovy(a)']/ul[@class='M(0) P(0)']/li[@class='Fl(start) D(b) Mb(10px)'][16]/label[@class='Ta(c) Pos(r) Va(tb) Pend(10px)']",
            # "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][2]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/div[@class='Py(15px)']/div[@class='Pstart(16px) Pend(20px) Mah(230px) Ovy(a)']/ul[@class='M(0) P(0)']/li[@class='Fl(start) D(b) Mb(10px)'][18]/label[@class='Ta(c) Pos(r) Va(tb) Pend(10px)']",
            "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][2]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/div[@class='Py(15px)']/div[@class='Pstart(16px) Pend(20px) Mah(230px) Ovy(a)']/ul[@class='M(0) P(0)']/li[@class='Fl(start) D(b) Mb(10px)'][19]/label[@class='Ta(c) Pos(r) Va(tb) Pend(10px)']"
        ]

        for target in target_list:
            industry = self.driver.find_element_by_xpath(target)
            industry.click()

        sector_close_button = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mb(5px) C($finDarkGray)'][4]/div[@class='D(ib) Bgc(white) Bdrs(3px)']/div[@class='D(ib) Bgc(white) Bdrs(3px) Pt(12px) Pb(9px) Pstart(18px) Pend(20px) Px(10px)--tab768 Mih(30px) Pos(r)'][2]/div[@class='D(ib) W(560px)--scrm W(510px)--scrl W(428px)!--tab768']/ul[@class='M(0) P(0) D(ib)']/li[@class='D(ib) Mb(3px) filterAdd']/div[@class='M(0) O(n):f D(ib) Bdrs(3px) Bgc($pillBgBlue):h C($finDarkGray) Fz(s)']/div[@class='D(ib) O(n):f Pt(6px) Pb(7px) Pstart(6px) Pend(7px) Bgc($extraLightBlue):f']/div[@id='dropdown-menu']/button[@class='Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close']")
        sector_close_button.click()

    def find_stock(self):
        find_stock_button = self.driver.find_element_by_xpath("/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/section[@id='screener-criteria']/div[@class='Bd Bdc($grey4) W(100%) Bgc($panelBackground) Pt(14px) Pb(20px) Bdrs(3px) Pos(r) Mt(45px) Bdrststart(0px)!']/div[@class='Mstart(28px) Pend(25px)']/div/div[@class='D(ib) Fl(start)']/div[@class='Mt(20px)']/button[@class='Bgc($actionBlue) C(white) Fw(500) Px(20px) Py(9px) Bdrs(3px) Bd(0) Fz(s) D(ib) Whs(nw) Miw(110px) Bgc($actionBlueHover):h']/span")
        find_stock_button.click()

        element_present = EC.presence_of_element_located((By.XPATH, "/html[@id='atomic']/body/div[@id='app']/div/div/div[@id='render-target-default']/main[@class='app']/div[@id='FIN-MainCanvas']/div[@class='Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3)']/div/div[@id='main-0-ScreenerDetail-Proxy']/section[@class='Pos(r)']/section[@class='Z(3) Va(t)']/div[2]/section[@id='screener-results']/div[@class='Pos(r)']/div[@class='Pos(a) Start(0) T(0) End(0) B(0) Z(6)']/div[@class='Mstart(a) Mend(a) W(560px) H(220px) Bgc(white) Bxsh($boxShadow) Bd Bdc($finLightGray) Bdrs(3px) Mt(80px)']/div[@class='Mstart(a) Mend(a) Pt(65px) Ta(c)']"))
        try:
            WebDriverWait(self.driver, 30).until(element_present)
            find_stock_button.click()
        except:
            pass

    def run(self):
        self.prepare_starting_page()
        self.enqueue_links()
