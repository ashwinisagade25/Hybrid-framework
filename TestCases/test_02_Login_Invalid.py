from selenium import webdriver
import pytest
from Utilities.BaseClass import Baseclass
from PageObjects.Loginpage import LoginPage
from Utilities import ExcelUtility
class Testlogin_Invalid(Baseclass):
    path="..\\TestData\\loginTestData.xlsx"
    

    def test002_invalidlogin(self):
        logger=Baseclass.clogger.getCustomLogger()
        loginpage = LoginPage(self.driver)
        self.rows=ExcelUtility.getRowCount(Testlogin_Invalid.path, "sheet1")
        
        for r in range(2,self.rows+1):
            self.user=ExcelUtility.readData(Testlogin_Invalid.path, "sheet1", r, 1)  
            self.passwd=ExcelUtility.readData(Testlogin_Invalid.path, "sheet1", r, 2)       
            logger.info("Verifying with Invalid Credentials")
            loginpage.setUserName(self.user)
            loginpage.setPassword(self.passwd)
            dashboardpage=loginpage.clickLogin()
            assert loginpage.verifyErrorMsg() is True
            logger.info("Verification with Invalid Credentials is pass")
            
            
            