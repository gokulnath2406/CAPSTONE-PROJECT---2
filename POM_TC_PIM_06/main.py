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
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Contact_details_button).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Street1).send_keys(Gokul_Data().Street1)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Street2).send_keys(Gokul_Data().Street2)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().City).send_keys(Gokul_Data().City)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().State_Province).send_keys(Gokul_Data().State_Province)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Zip_postalCode).send_keys(Gokul_Data().Zip_postalCode)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Home).send_keys(Gokul_Data().Home)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Mobile).send_keys(Gokul_Data().Mobile)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Work).send_keys(Gokul_Data().Work)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Work_Email).send_keys(Gokul_Data().Work_Email)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Other_Email).send_keys(Gokul_Data().Other_Email)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Save1).click()
        



        

        





s = Gokul(Gokul_Data().url)


s.login()
