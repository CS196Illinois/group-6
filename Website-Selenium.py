from selenium import webdriver

path = "C:\\WebDriver\\bin\\chromedriver.exe"  # this should be the path of your chromedriver

driver = webdriver.Chrome(path)


driver.get("https://illinois.edu/about/quadcam.html")
print(driver.title)


# driver.quit()

