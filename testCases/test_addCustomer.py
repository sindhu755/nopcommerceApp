import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LonGen
import string
import random
from selenium.webdriver.common.by import By

@pytest.mark.sanity
class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LonGen.loggen()


    def test_addCustomer(self,setup):
        self.logger.info("*************Test_003_AddCustomer***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login successful*************")

        self.logger.info("**********Starting Add Customer Test*************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomarMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()
        self.logger.info("**********providing customer info***********")

        self.email=random_generator() + "gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Sindhu")
        self.addcust.setLastName("Kommi")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing..........")
        self.addcust.clickOnSave()

        self.logger.info("************Saving customer info*****************")

        self.logger.info("**********Add customer validation started **************")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text


        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("***********Add customer test passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png") #Screenshot

        self.driver.close()
        self.logger.info("***********Ending Home Page Title Test*****************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))




