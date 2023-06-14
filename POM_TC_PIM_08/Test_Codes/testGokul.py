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
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Edit_Emp).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Dependents).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Dependents_add).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Name).send_keys(Gokul_Data().Name)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Date_of_birth).send_keys(Gokul_Data().Date_of_birth)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Save).click()
        print("filled all Dependents details and validated successfully")







