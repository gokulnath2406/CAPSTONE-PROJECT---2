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
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Emp_Edit).click()
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().Firstname).send_keys(Gokul_Data().First_name)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().Lastname).send_keys(Gokul_Data().Last_name)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Nickname).send_keys(Gokul_Data().Nickname)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Other_id).send_keys(Gokul_Data().Other_id)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Driver_License_Number).send_keys(Gokul_Data().Driver_License_Number)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().License_Expiry_Date).send_keys(Gokul_Data().License_Expiry_Date)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Date_of_Birth).send_keys(Gokul_Data().Date_of_Birth)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Military_Service).send_keys(Gokul_Data().Military_Service)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Save01).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Save02).click()
        print("Filled all personal details and validated")









