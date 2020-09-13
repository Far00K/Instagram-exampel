from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import csv
import time
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


Username = ''
Password = ''

url = "https://www.instagram.com/freshlycosmetics/"
Path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get(url)
time.sleep(2)

btn = driver.find_element_by_class_name('tdiEy').click()
time.sleep(2)
driver.find_element_by_xpath("//input[@type='text']").send_keys(Username) # Type in the username in username field 
driver.find_element_by_xpath("//input[@type='password']").send_keys(Password) # Type in the password in password field 
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)
driver.find_element_by_class_name('sqdOP').click()
