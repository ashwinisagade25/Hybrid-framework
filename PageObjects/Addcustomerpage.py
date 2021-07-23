from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from select import select
import time


class AddCustomerPage:
    
    link_expand_css="i.fa-plus"
    txtbx_email_id="Email"
    txtbx_password_id="Password"
    txtbx_fname_id="FirstName"
    txtbx_lname_id="LastName"
    rdobtn_Female_id="Gender_Female"
    rdobtn_Male_id="Gender_Male"
    txtbx_DoB_id="DateOfBirth"
    dtpicker_DoB_css="span.k-datepicker span span.k-select"
    txtbx_companyname_id="Company"
    chkbx_Tax_id="IsTaxExempt"
    listbx_newsletter_xpath="//div[@class='input-group-append']//div[@class='k-multiselect-wrap k-floatwrap']"
    list_newslwtteritem1_xpath="//li[contains(text(),'Your store name')]"
    list_newslwtteritem2_xpath="//li[contains(text(),'Test store 2')]"
    listbx_custroles_xpath="//div[@class='k-widget k-multiselect k-multiselect-clearable']//span[contains(text(),'Registered')]"
    listopt_custroles_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']//li"
    drpdwn_vendorid_id="VendorId"
    chkbx_active_id="Active"
    txtarea__admincmt_id="AdminComment"
    btn_save_css="button[name='save']"
    alert_successmsg_css="div.alert-success "
    
    def __init__(self,driver):
        self.driver=driver
        
         
    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtbx_email_id).send_keys(email)
        
    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtbx_password_id).send_keys(password)
    
    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txtbx_fname_id).send_keys(fname)
    
    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txtbx_lname_id).send_keys(lname)
        
    def selectGender(self,gender):
        if gender=="Female":
            self.driver.find_element_by_id(self.rdobtn_Female_id).click()
        else:
            self.driver.find_element_by_id(self.rdobtn_Male_id).click()
        
    def setDoB(self,dob):
        self.driver.find_element_by_id(self.txtbx_DoB_id).send_keys(dob)
        
    def setCompanyName(self,company):
        self.driver.find_element_by_id(self.txtbx_companyname_id).send_keys(company)
        
    def checkIsTaxExempt(self):
        self.driver.find_element_by_id(self.chkbx_Tax_id).click()
        
    def clickNewsletterbox(self):
        self.driver.find_element_by_xpath(self.listbx_newsletter_xpath).click()
        
    def selectNewsletteroption(self,newsltropt):
        
        newsopt1=self.driver.find_element_by_xpath(self.list_newslwtteritem1_xpath).text
        newsopt2=self.driver.find_element_by_xpath(self.list_newslwtteritem2_xpath).text
        if newsltropt == newsopt1:
            self.driver.find_element_by_xpath(self.list_newslwtteritem1_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.list_newslwtteritem2_xpath).click()
    
    def clickCustRolebox(self):
        self.driver.find_element_by_xpath(self.listbx_custroles_xpath).click()
        
    def selectCustRoleOpt(self,role):
        roles=self.driver.find_elements_by_xpath(self.listopt_custroles_xpath)
        for r in roles:
            print(r.text)
            if r.text==role:
                 self.driver.find_element_by_xpath(self.listopt_custroles_xpath+"[contains(text(),'"+role+"')]").click()   
    
    def selectVendorId(self,vendorid):
        print("vendor=",vendorid)
        vendor=Select(self.driver.find_element_by_id(self.drpdwn_vendorid_id)) 
        vendor.select_by_visible_text(vendorid)
        
    def checkActive(self):
        self.driver.find_element_by_id(self.chkbx_active_id).click()
        
    def setAdminComment(self,comment):
        self.driver.find_element_by_id(self.txtarea__admincmt_id).send_keys(comment)
        
    def clickSave(self):
        self.driver.find_element_by_css_selector(self.btn_save_css).click()
        return 
    
    def verifySucceseMsg(self):
        return self.driver.find_element_by_css_selector(self.alert_successmsg_css).text
    
    def Isexpanded(self):
        if self.driver.find_element_by_id(self.txtbx_email_id).is_displayed():
            pass
        else:
            self.driver.find_element_by_css_selector(self.link_expand_css).click()
        
        
    
              
        
       
        
        