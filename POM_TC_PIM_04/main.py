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
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().edit_Emp).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Contact_Details).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Emergency_contact).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Dependents).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Immigration).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Job).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Salary).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Tax_exemptions).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Report_to).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Qualifications).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Memberships).click()

        





s = Gokul(Gokul_Data().url)


s.login()

