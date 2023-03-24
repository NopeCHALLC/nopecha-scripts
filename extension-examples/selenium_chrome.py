import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print('webdriver_manager not found. installing...')
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager


NOPECHA_KEY = "YOUR KEY HERE"

options = webdriver.chrome.options.Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

# Download and load the NopeCHA extension
with open('ext.crx', 'wb') as f:
    f.write(requests.get('https://nopecha.com/f/ext.crx').content)
options.add_extension('ext.crx')

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

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
