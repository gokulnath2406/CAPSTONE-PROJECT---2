from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Gokul_Data
from Test_Locators.locators import Gokul_Locators
import pytest


class Test_Gokul:


    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        

    def test_login(self, boot):
        self.driver.get(Gokul_Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().username_input_box).send_keys(Gokul_Data().username)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().password_input_box).send_keys(Gokul_Data().password)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().submit_button).click()
        print("The user is logged in successfully")
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
        print("Employee list tabs present and tested successfully")





