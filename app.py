import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with open("config.json") as config:
    cfg = json.load(config)

driver = webdriver.Chrome()

driver.get(cfg["url"])

try:
    stp = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'ui-button-text ui-c') and text()='Stop']")))
    if stp:
        stp.click()
        #driver.wait() doesn't work
        time.sleep(1)


except:
    username = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='containerall']/form/table/tbody/tr[1]/td[2]/input")))
    password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='containerall']/form/table/tbody/tr[2]/td[2]/input")))

    login_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='containerall']/form/table/tbody/tr[3]/td/input")))


    username.send_keys(cfg[username])
    password.send_keys(cfg[password])

    login_button.click()
    driver.implicitly_wait(5)

    stop_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'ui-button-text ui-c') and text()='Stop']")))

    stop_button.click()
    driver.implicitly_wait(5)

finally:
    driver.quit()

