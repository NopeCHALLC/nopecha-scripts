import os
import requests
import time
import zipfile
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.service import Service as ChromeService

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print('webdriver_manager not found. installing...')
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager


NOPECHA_KEY = "YOUR KEY HERE"

options = uc.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

with open('chrome.zip', 'wb') as f:
    f.write(requests.get('https://github.com/NopeCHA/NopeCHA/releases/latest/download/chrome.zip').content)
with zipfile.ZipFile('chrome.zip', 'r') as f:
    f.extractall('nopecha')
options.add_argument(f"--load-extension={os.getcwd()}/nopecha")

driver = uc.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
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
