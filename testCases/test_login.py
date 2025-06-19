from selenium import webdriver
import pytest

from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LonGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LonGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_homePageTitle(self,setup):
        self.logger.info("***************Test_001_Login*************")
        self.logger.info("************Verifying Home Page Title************")

        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="nopCommerce demo store. Login":
            assert True
            self.logger.info("***********Home page title test is passed**********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************Home page title test is failed***************")
            assert False
            # self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self,setup):
        self.logger.info("************Verifying Login Test**************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        # self.driver.close()
        # print("Actual title is:",act_title)

        if act_title=="Dashboard / nopCommerce administration":
            print("Actual title is:",act_title)
            assert True
            self.logger.info("************Login test is passed**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************Login test is failed**************")
            assert False





