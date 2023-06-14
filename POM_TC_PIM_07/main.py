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
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Emp_edit).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Emergency_Contacts).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Emergency_Contacts_add).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Name).send_keys(Gokul_Data().Name)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Relationship).send_keys(Gokul_Data().Relationship)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Home_telephone).send_keys(Gokul_Data().Home_telephone)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Mobile).send_keys(Gokul_Data().Mobile)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Work_telephone).send_keys(Gokul_Data().Work_telephone)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Save).click()
        print('filled all Emergency Contacts and validated successfully')





s = Gokul(Gokul_Data().url)


s.login()

