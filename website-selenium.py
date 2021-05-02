from selenium import webdriver
from selenium.webdriver.support.ui import *
import time

path = "C:\\WebDriver\\bin\\chromedriver.exe"  # this should be the path of your chromedriver

driver = webdriver.Chrome(path)
driver.get("https://quadcamproxy.admin.illinois.edu/video.html")

js = """
return document.getElementById('video_image_video').src
"""

while True:
    try:
        last_url = driver.execute_script(js)
        if driver.execute_script(js) != last_url:
            current_url = driver.execute_script(js)
            print(current_url)
            last_url = current_url
    except:
        WebDriverWait(driver, 10)

# driver.quit()

