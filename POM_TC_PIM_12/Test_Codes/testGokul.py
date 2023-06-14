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
        print("filled all salary and deposit details and validated successfully")
        






