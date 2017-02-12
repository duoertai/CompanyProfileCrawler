from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from Queue import Queue
import re
import threading

class TargetFinder(threading.Thread):
    def __init__(self, queue):
        self.driver = webdriver.PhantomJS()
        self.queue = queue

    def prepare_starting_page(self):
        pass
