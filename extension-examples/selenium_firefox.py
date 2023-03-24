import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

try:
    from webdriver_manager.firefox import GeckoDriverManager
except:
    print('webdriver manager not found. installing...')
    os.system('pip install webdriver-manager')
    from webdriver_manager.firefox import GeckoDriverManager


NOPECHA_KEY = "YOUR KEY HERE"

# Download and load the NopeCHA extension
with open('ext.xpi', 'wb') as f:
    f.write(requests.get('https://nopecha.com/f/ext.xpi').content)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.install_addon(f"{os.getcwd()}/ext.xpi")
driver.get(f"https://nopecha.com/setup#{NOPECHA_KEY}")
driver.get('https://accounts.hcaptcha.com/demo')

try:
    print('press CTRL+C to exit')
    print('\n')
    print(f"if your browser is not solving, check if this is your correct key: {NOPECHA_KEY}")
    print('if not, please edit this code to replace "YOUR KEY HERE" with your key')
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    driver.quit()
