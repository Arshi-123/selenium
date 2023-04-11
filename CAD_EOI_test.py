from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import os





s = Service('/usr/local/bin/geckodriver')
options = webdriver.FirefoxOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
#options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")


driver = webdriver.Firefox(service=s, options=options)
# navigate to eoi webpage
driver.get("https://www.uts.edu.au/")

driver.find_element(By.XPATH,"/html/body/div[1]/header/div[4]/nav/ul/li[1]/span").click()

#quit file
driver.quit()
