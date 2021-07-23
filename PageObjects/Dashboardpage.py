
from selenium import webdriver
from PageObjects.Addcustomerpage import AddCustomerPage

class DashboardPage:
    btn_logout_link="Logout"
    link_customersmenu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_addnew_linktext="Add new"
    
    def __init__(self,driver):
        self.driver=driver
    
    def clickLogout(self):
        btn_logout=self.driver.find_element_by_link_text(DashboardPage.btn_logout_link)
        btn_logout.click()
        
    def clickCustomersMenu(self):
        self.driver.find_element_by_xpath(self.link_customersmenu_xpath).click()
           
        
    def clickCustomers(self):
        self.driver.find_element_by_xpath(self.link_customers_xpath).click()
        
    
    def clickAddNew(self):
        self.driver.find_element_by_link_text(self.link_addnew_linktext).click()
        self.addcustomer=AddCustomerPage(self.driver)
        return self.addcustomer
        