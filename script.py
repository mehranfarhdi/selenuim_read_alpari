from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import time
import base64
import json

# Main Function
if __name__ == "__main__":
    # Enable Performance Logging of Chrome.
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    # Create the webdriver object and pass the arguments
    options = webdriver.ChromeOptions()

    # Chrome will start in Headless mode
    options.add_argument('headless')
    # options.add_argument('--proxy-server=socks5://127.0.0.1:1080')
    # Ignores any certificate errors if there is any
    options.add_argument("--ignore-certificate-errors")

    # Startup the chrome webdriver with executable path and
    # pass the chrome options and desired capabilities as
    # parameters.
    driver = webdriver.Chrome(chrome_options=options,
                              desired_capabilities=desired_capabilities)
    # Send a request to the website and let it load
    while True:
        driver.get("https://alpariforex.org/en/invest/pamm/530350/#pamm-leverage")

        # Sleeps for 10 seconds
        time.sleep(3)

        # Gets all the logs from performance in Chrome
        logs_raw = driver.get_log("performance")
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

        def log_filter(log_):
            return (
                # is an actual response
                    log_["method"] == "Network.responseReceived"
                    # and json
                    and "json" in log_["params"]["response"]["mimeType"]
            )

        for log in filter(log_filter, logs):
            request_id = log["params"]["requestId"]
            resp_url = log["params"]["response"]["url"]
            if (resp_url == "https://alpariforex.org/api/en/pamm/other/506176/active/"):
                print(f"Caught {resp_url}")
                data = driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
                parsed_body = json.loads(data['body'])
                print(data['body'])
                send = requests.post("https://api.xfxfund.com/api/v1/brokers/broker/", json=parsed_body)

        time.sleep(3600)