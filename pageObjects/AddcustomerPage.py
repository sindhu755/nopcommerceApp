import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    #Add customer page
    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[normalize-space()='Add new']"
    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtCompanyName_xpath="//input[@id='Company']"
    txtNewsLetter_xpath="//span[@aria-expanded='true']//input[@role='searchbox']"
    lstitemnopCommerce_xpath="//li[@id='select2-SelectedNewsletterSubscriptionStoreIds-result-ua6t-1']"
    txtCustomerRoles_xpath="//span[@aria-expanded='true']//ul[@class='select2-selection__rendered']"
    lstitemRegistered_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-wy1r-3']"
    lstitem_administrators_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-wy1r-3']"
    lstitemForum_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-n9ql-2']"
    lstitemGuest_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-epwg-4']"
    lstitemVendors_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-rp0k-5']"
    drpmgrofVendor_xpath="//select[@id='VendorId']"
    txtAdminContent_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomarMenu(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.lnkCustomers_menu_xpath))).click()
        # self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role== 'Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_administrators_xpath)
        elif role == 'Guests':
            #Here user can be Registered (or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//span[@role='presentation']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0];",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrofVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.ID, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID, self.txtLastName_xpath).send_keys(lname)
    def setCompanyName(self,comname):
        self.driver.find_element(By.ID, self.txtCompanyName_xpath).send_keys(comname)
    def setAdminContent(self,content):
        self.driver.find_element(By.ID, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.ID, self.btnSave_xpath).click()




























