import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# serv_obj = Service("/devad_pyiy/Selenium/chromedriver-win32")
# webdriver.Chrome(service=serv_obj)
# time.sleep()

# driver = webdriver.Chrome()
driver = webdriver.Edge()
# driver = webdriver.Firefox()
driver.get("https://sastra.verandahighered.com/login")
# driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.CLASS_NAME,"userNameInput").send_keys("dd7581deva@gmail.com")
driver.find_element(By.CLASS_NAME,"passwordInput").send_keys("Ssuccess2312@!")
driver.find_element(By.CLASS_NAME,"login").click()
time.sleep(7)
driver.find_element(By.LINK_TEXT,"Master of Business Administration (July 2023) - Semester III").click()
time.sleep(5)

# serv_obj = Service("/devad_pyiy/Selenium/chromedriver-win32")
# webdriver.Chrome(service=serv_obj)
# time.sleep()