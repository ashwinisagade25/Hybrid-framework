from selenium import webdriver
import pytest
from Utilities.BaseClass import Baseclass
from Utilities.readProperties import ReadConfig
from PageObjects.Loginpage import LoginPage
import random
import string

class CommonUIMethods(Baseclass):
    
    def login(self):
        self.logger=Baseclass.clogger.getCustomLogger()
        loginpage = LoginPage(self.driver)
        self.logger.info("Verifying with Valid Credentials")
        loginpage.setUserName(ReadConfig.getConfigData("username"))
        loginpage.setPassword(ReadConfig.getConfigData("password"))
        dashboardpage=loginpage.clickLogin()
        assert loginpage.getPageTitle()=="Dashboard / nopCommerce administration"
        self.logger.info("Verification with Valid Credentials is pass")
        return dashboardpage
        
    def logout(self):
        self.dashboardpage.clickLogout()
        
    def randomGenerator(self,size=8,chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    

