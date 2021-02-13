import time
import json

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# WebDriverWait(browser,10)
file = open('userinput.json', "r")
userdata = json.loads(file.read())
global city_temp
city_temp=[]
for city in userdata['City']:
    try:
        browser = webdriver.Chrome()
        browser.get("https://weather.com/")
        browser.maximize_window()
        search_element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "LocationSearch_input")))
        search_element.click()
        search_element.send_keys("%s" % city)
        search_element.click()
        city_searchbutton = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//div/button[@id='LocationSearch_listbox-0']" )))
        city_searchbutton.click()
        city_page = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1[class='CurrentConditions--location--1Ayv3']")))
        city_tempa = browser.find_element_by_xpath("//span[@class='CurrentConditions--tempValue--3KcTQ']")
        print(city_tempa.text)
        degree = city_tempa.text
        degree = degree.rstrip('°')
        print(degree)
        city_temp.append(degree)

    finally:
        browser.quit()
