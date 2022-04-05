from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest


class TestLogin():
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver=webdriver.Chrome(executable_path='C:/Users/ddiva/PycharmProjects/AutomationFramework/drivers/chromedriver.exe')
        driver.implicitly_wait(5)
        driver.maximize_window()
    #Teardown gets done here
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.ID, "txtUsername").clear()
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").clear()
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.ID, "btnLogin").send_keys(Keys.ENTER)

    def test_logout(self,test_setup):
        driver.find_element(By.ID, "welcome").send_keys(Keys.ENTER)
        driver.find_element(By.LINK_TEXT, "Logout").send_keys(Keys.ENTER)