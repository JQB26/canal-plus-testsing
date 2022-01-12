import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_binary = r"C:\path\to\chromedriver.exe"
options = Options()
options.add_argument('--disable-gpu')  


class TestLoggingin():
  def setup_method(self):
    self.driver = webdriver.Chrome(chrome_options = options, executable_path=chrome_driver_binary)
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_loggingin(self):
    self.driver.get('https://www.canalplus.com')
    self.driver.find_element(By.XPATH, "//*[@id=\"accept-btn\"]").click()
    self.driver.find_element(By.XPATH, "//*[@id=\"currentProfile_onclick\"]/div").click()
    self.driver.find_element(By.XPATH, "//*[@id=\"Zaloguj się_onclick\"]").click()
    self.driver.find_element(By.XPATH, "//*[@id=\"username\"]").send_keys("username")
    self.driver.find_element(By.XPATH, "//*[@id=\"password\"]").send_keys("password")
    self.driver.find_element(By.XPATH, "//*[@id=\"fm1\"]/div[2]/input[4]").click()
  

if __name__ == "__main__":
  t = TestLoggingin()
  t.setup_method()
  t.test_loggingin()
  time.sleep(3)
  t.teardown_method()