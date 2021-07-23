from selenium import webdriver
import time
import pytest
from Utilities.BaseClass import Baseclass
from PageObjects.Addcustomerpage import AddCustomerPage
from Utilities.readProperties import ReadConfig
from Utilities.CommonUI import CommonUIMethods
from Utilities import ExcelUtility


class TestRegister_valid(Baseclass):
    path="..\\TestData\\RegisterValidTestData.xlsx"
    
    def test001_validRegister(self):
        
        logger=Baseclass.clogger.getCustomLogger()
        logger.info("Login with valid credentials")
        dashboardpage=CommonUIMethods.login(self)
        time.sleep(3)
        dashboardpage.clickCustomersMenu()
        time.sleep(3)
        dashboardpage.clickCustomers()
        logger.info("clicked customers link")
        
        time.sleep(3)
        
        addcustomer=dashboardpage.clickAddNew()
        time.sleep(3)        
        logger.info("Registration with valid dataset")
        email=CommonUIMethods.randomGenerator(self)+"@gmail.com"
        addcustomer.Isexpanded()
        addcustomer.setEmail(email)
        
        password=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 1)
        fname=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 2)  
        lname=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 3)  
        gender=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 4)  
        dob=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 5)  
        company=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 6)  
        newsltropt=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 7)
        role=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 8)  
        vendorid=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 9)
        comment=ExcelUtility.readData(TestRegister_valid.path, "sheet1", 2, 10) 
           
        addcustomer.setPassword(password)
        addcustomer.setFirstName(fname)
        addcustomer.setLastName(lname)
        addcustomer.selectGender(gender)
        addcustomer.setDoB(dob)
        addcustomer.setCompanyName(company)
        addcustomer.checkIsTaxExempt()
        addcustomer.clickNewsletterbox()
        time.sleep(3)
        addcustomer.selectNewsletteroption(newsltropt)
        addcustomer.clickCustRolebox()
        time.sleep(3)
        addcustomer.selectCustRoleOpt(role)
        addcustomer.selectVendorId(vendorid)
        addcustomer.checkActive()
        addcustomer.setAdminComment(comment)
        addcustomer.clickSave()
        logger.info("Saving with valid data")
        time.sleep(5)
        
        assert "successfully" in addcustomer.verifySucceseMsg() 
        logger.info("Registration with valid data is passed")
            
        
        
        
        
        
        