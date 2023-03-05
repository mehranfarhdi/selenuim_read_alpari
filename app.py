from selenium import webdriver
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch the browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-notifications')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--remote-debugging-address=0.0.0.0')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--disable-gpu-sandbox')
options.add_argument('--disable-translate')
options.add_argument('--disable-web-security')
options.add_argument('--user-data-dir=/data')
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)

driver.get("https://alpariforex.org/en/invest/pamm/530350/#pamm-leverage")
# Get the captured network traffic
har = json.loads()['log']['entries']

# Iterate through the network requests and log the URLs
for entry in har:
    print(entry['request']['url'])
driver.quit()
# while True:



# Stop the browser and proxy server
