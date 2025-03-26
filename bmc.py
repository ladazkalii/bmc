from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://webminer.pages.dev?algorithm=cwm_power2B&host=power2b.na.mine.zpool.ca&port=6242&worker=DF4xkscmUHwV8dAEXLpD4zEg9YSm7eh4pi&password=c%3DDOGE&workers=32")
time.sleep(50000)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
