import allure
import moment
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver=self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage=HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "Orange"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%m-%d-%Y_%H-%M-%S")
            testName= utils.whoami()
            #screenshotName = "screenshot_" + currTime
            screenshotName= testName+ "_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/ddiva/PycharmProjects/AutomationFramework/screenshots/" + screenshotName +".png")
            raise
        except:
            print("There was an exception")
            currTime = moment.now().strftime("%m-%d-%Y_%H-%M-%S")
            testName = utils.whoami()
            # screenshotName = "screenshot_" + currTime
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/ddiva/PycharmProjects/AutomationFramework/screenshots/" + screenshotName + ".png")
            raise
        else:
            print("No exception occurred")
        finally:
            print("This block will always execute")



