from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Gokul_Data
from Test_Locators.locators import Gokul_Locators
from selenium.webdriver.support.ui import Select


class Gokul:
   
    def __init__(self, url):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)
   
    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().username_input_box).send_keys(Gokul_Data().username)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().password_input_box).send_keys(Gokul_Data().password)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().submit_button).click()
        print("The user is logged in successfully")
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Admin).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_field).send_keys(Gokul_Data().search1)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().User_management).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Users).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().User_role).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Admin_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Status_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Status_Enable).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Search_button).click()
        print("In User role Admin is selected and Status selected as Enabled successfully")
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().ESS).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Status_disable).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Search_button).click()
        print('In User role ESS is selected and Status selected as Disabled successfully')
        


        
s = Gokul(Gokul_Data().url)
s.login()


