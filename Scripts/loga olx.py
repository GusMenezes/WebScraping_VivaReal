import undetected_chromedriver as uc
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1366,768')
options.add_argument("'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'")

url = 'https://www.olx.com.br/'

navegador = uc.Chrome(options=options)
navegador.get(url)


navegador.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/div[2]/ul/li[5]/a').click()


email_element = navegador.find_element(By.CSS_SELECTOR, '#input-1')
email_element.send_keys('ginga.olx@gmail.com')
time.sleep(2)
navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/button').click()
time.sleep(3)
password_element = navegador.find_element(By.CSS_SELECTOR, '#password-input')
password_element.send_keys('')
navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[3]/button[2]').click()
time.sleep(30)
