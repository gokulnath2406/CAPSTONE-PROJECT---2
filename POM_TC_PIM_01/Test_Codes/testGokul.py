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
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search1)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search2)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search3)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search4)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search5)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search6)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search7)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search8)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).send_keys(Gokul_Data().search9)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().search_Field).clear()

        print("MENU options displayed successfully")



