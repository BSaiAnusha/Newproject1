# Keyword Driven Testing Framework


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from yaml_functions import Anusha_YAML

file_name = 'D:\\workspace\\POM\\config.yaml'


s = Anusha_YAML(file_name)


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get(s.yaml_reader()['url'])
driver.implicitly_wait(10)


driver.find_element(by=By.NAME, value=s.yaml_reader()['username_locator']).send_keys(s.yaml_reader()['username'])
driver.find_element(by=By.NAME, value=s.yaml_reader()['password_locator']).send_keys(s.yaml_reader()['password'])
driver.find_element(by=By.XPATH, value=s.yaml_reader()['submit_button_locator']).click()
