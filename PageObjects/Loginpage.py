from selenium import webdriver
from PageObjects.Dashboardpage import DashboardPage

class LoginPage:
    txt_username_id="Email"
    txt_password_id="Password"
    btn_login_css="button[type='submit']"
    error_msg_css="div.message-error"
    
    def __init__(self,driver):
        self.driver=driver
        
    def setUserName(self,username):
        txt_username=self.driver.find_element_by_id(LoginPage.txt_username_id)
        txt_username.clear()
        txt_username.send_keys(username)
        
    def setPassword(self,password):
        txt_password=self.driver.find_element_by_id(LoginPage.txt_password_id)
        txt_password.clear()
        txt_password.send_keys(password)
        
    def clickLogin(self):
        btn_login = self.driver.find_element_by_css_selector(LoginPage.btn_login_css)
        btn_login.click()
        dashboardpage = DashboardPage(self.driver)
        return dashboardpage
        
    def getPageTitle(self):
        return self.driver.title
    
    def verifyErrorMsg(self):
        error_msg=self.driver.find_element_by_css_selector(LoginPage.error_msg_css)
        return error_msg.is_displayed()
    