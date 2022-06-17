from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from file_path import *

s=Service( r'C:\Users\ushur\Desktop\Selenium\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.maximize_window()
url='https://www.hotstar.com/in'
browser.get(url)
sleep(3)
browser.find_element(By.ID, 'searchField').send_keys('SUPER SINGER')
sleep(3)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div/div[2]/div/div[4]/div[2]/div[4]/article/a/div[2]').click()
sleep(3)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/a/article/div[2]/div[1]').click()
sleep(2)
'''
browser.close()
browser.find_element(By.XPATH, '').click()
'''