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
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_field).send_keys(Gokul_Data().search1)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Add_employee).click()
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().First_name).send_keys(Gokul_Data().Firstname)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().Last_name).send_keys(Gokul_Data().Lastname)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Create_login_details).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().username_input_box1).send_keys(Gokul_Data().username_Emp)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().password_input_box1).send_keys(Gokul_Data().password_Emp1)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().confirm_password_input_box1).send_keys(Gokul_Data().password_Emp2)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Emp_save_Button).click()
        print("User Add Employee successfully")






