import json

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the proxy
# proxy = Proxy({
#     'proxyType': ProxyType.MANUAL,
#     'socksProxy': 'socks5://127.0.0.1:1080' # Replace with your own proxy settings
# })

# Set up the Chrome driver with the proxy
options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=%s' % proxy.socksProxy)
driver = webdriver.Chrome(options=options)

# Load the page
driver.get("https://alpariforex.org/en/invest/pamm/530350/#pamm-leverage")

# Open the DevTools window and switch to it
time.sleep(10)

# Gets all the logs from performance in Chrome
logs = driver.get_log("performance")

# Opens a writable JSON file and writes the logs in it
with open("network_log.json", "w", encoding="utf-8") as f:
    f.write("[")

    # Iterates every logs and parses it using JSON
    for log in logs:
        network_log = json.loads(log["message"])["message"]

        # Checks if the current 'method' key has any
        # Network related value.
        if ("Network.response" in network_log["method"]
                or "Network.request" in network_log["method"]
                or "Network.webSocket" in network_log["method"]):
            # Writes the network log to a JSON file by
            # converting the dictionary to a JSON string
            # using json.dumps().
            f.write(json.dumps(network_log) + ",")
    f.write("{}]")

print("Quitting Selenium WebDriver")
driver.quit()

# Read the JSON File and parse it using
# json.loads() to find the urls containing images.
json_file_path = "network_log.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    logs = json.loads(f.read())

# Iterate the logs
for log in logs:

    # Except block will be accessed if any of the
    # following keys are missing.
    try:
        # URL is present inside the following keys
        url = log["params"]["request"]["url"]

        # Checks if the extension is .png or .jpg
        if url == "https://alpari.com/api/en/pamm/other/506176/active/":
            print(url, end='\n\n')
    except Exception as e:
        pass