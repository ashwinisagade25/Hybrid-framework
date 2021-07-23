import pytest
from selenium import webdriver
from Utilities.readProperties import ReadConfig 

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome")
    


@pytest.fixture(scope="class")
def browserSetup(request):
    browsername = request.config.getoption("browser_name")
    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
       
        
    elif browsername == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\drivers\\geckodriver.exe")
        
    driver.get(ReadConfig.getConfigData("appURL"))
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    


