from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

word = ''
num = 0
content = ''

word = input('請輸入關鍵字:')
num = input('請輸入字數(1000以內):')
while int(num) > 1000 :
    num = input('錯誤 請重新輸入字數:')
print('產生中...')

s = Service("D:/Software/webdrivers/chromedriver.exe")
opts = Options()
opts.add_argument("headless") 
driver = webdriver.Chrome(service=s , options = opts)

driver.get('https://howtobullshit.me/')
driver.find_element(By.ID, 'topic').send_keys(word)
driver.find_element(By.ID, 'minlen').send_keys(num)
driver.find_element(By.ID, 'btn-get-bullshit').click()

time.sleep(5)

content = driver.find_element(By.ID, 'content').text

print(content)

