from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

sgr = 'RU.23.КК.08.008.Е.000964.08.14'
link = 'https://nsi.eaeunion.org/portal/1995'

options = Options()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get(link)
filter_button = driver.find_element(By.XPATH, '//*[@id="dictionary-view"]/div[1]/div[3]/div/div/div[1]/table/thead/tr/th[2]/div/div/button/span')
filter_button.click()
input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/input')))
input_field.send_keys(sgr)
apply_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/button[2]/span[1]')
apply_button.click()
result = driver.find_element(By.XPATH, '//*[@id="dictionary-view"]/div[1]/div[3]/div/div/div[1]/table/tbody/tr/td[2]/div/div/span')
ActionChains(driver).double_click(result).perform()
time.sleep(5)
url = driver.current_url
print(url)

driver.quit()