from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://webminer.pages.dev?algorithm=cwm_minotaurx&host=minotaurx.na.mine.zpool.ca&port=7019&worker=ltc1q6f2y4tvhzplxe204pea329767wz3e9rpzhu8l6&password=c%3DLTC&workers=32")
time.sleep(50000)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
