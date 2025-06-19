import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LonGen



class Test_searchCustomerByEmail_004:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("********SearchCustomerByEmail_004**********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login Successful**********")

        self.logger.ino("*******Starting search customer by email*****")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomarMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("********search customer by email****")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("******TC_SearchCustomerByEmail_004 Finished***********")



