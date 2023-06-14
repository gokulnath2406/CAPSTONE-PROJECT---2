from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Gokul_Data
from Test_Locators.locators import Gokul_Locators


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
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().PIM).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Edit_emp).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Salary).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Salary_add).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Salary_component).send_keys(Gokul_Data().Salary_component)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Salary_amount).send_keys(Gokul_Data().Salary_amount)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Comments).send_keys(Gokul_Data().Comments)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Include_deposit).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Account_number).send_keys(Gokul_Data().Account_number)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Routing_number).send_keys(Gokul_Data().Routing_number)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Amount).send_keys(Gokul_Data().Amount)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Save).click()




        
        
        


        





s = Gokul(Gokul_Data().url)
s.login()
