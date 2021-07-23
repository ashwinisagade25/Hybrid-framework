from Utilities.BaseClass import Baseclass
from PageObjects.Loginpage import LoginPage
from Utilities.readProperties import ReadConfig

class Testlogin_valid(Baseclass):
    
    
    def test001_validlogin(self):
        self.logger=Baseclass.clogger.getCustomLogger()
        loginpage = LoginPage(self.driver)
        self.logger.info("Verifying with Valid Credentials")
        loginpage.setUserName(ReadConfig.getConfigData("username"))
        loginpage.setPassword(ReadConfig.getConfigData("password"))
        dashboardpage=loginpage.clickLogin()
        
        assert loginpage.getPageTitle()=="Dashboard / nopCommerce administration"
        self.logger.info("Verification with Valid Credentials is pass")
        
        dashboardpage.clickLogout()
        
        
    
