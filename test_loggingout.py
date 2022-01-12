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

class TestLoggingout():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loggingout(self):
    self.driver.get("/")
    self.driver.find_element(By.XPATH, "//*[@id=\"profileAvatar_onclick\"]/picture/img").click()
    self.driver.find_element(By.XPATH, "//*[@id=\"Wyloguj się_onclick\"]").click()
