from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(r"C:\Users\koga\Documents\chromedriver_win32\chromedriver.exe")
driver.get("http://pythonscraping.com/pages/files/form.html")
firstname_field = driver.find_element_by_name("firstname")
lastname_field = driver.find_element_by_name("lastname")
submit_button = driver.find_element_by_id("submit")

"""
#Method 1
firstname_field.send_keys("Ryan")
lastname_field.send_keys("Mitchell")
submit_button.click()
"""
"""
#Method 2
actions = ActionChains(driver).click(firstname_field) \
    .send_keys("Ryan").click(lastname_field).send_keys("Mitchell").send_keys(Keys.RETURN)
actions.perform()
"""

driver.close()