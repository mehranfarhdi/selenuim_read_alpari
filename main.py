from selenium import webdriver
import json

# # Start the browsermob-proxy server
# server = Server("path/to/browsermob-proxy/bin/browsermob-proxy")
# server.start()
# proxy = server.create_proxy()
#
# # Configure the browser to use the proxy
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server={0}".format(proxy.proxy))

# Start the browser and navigate to a URL
driver = webdriver.Chrome()

while True:
    try:
        driver.get("https://alpariforex.org/en/invest/pamm/530350/#pamm-leverage")
        # Get the captured network traffic
        har = json.loads()['log']['entries']

        # Iterate through the network requests and log the URLs
        for entry in har:
            print(entry['request']['url'])
        driver.quit()
    except:
        pass
# Stop the browser and proxy server
