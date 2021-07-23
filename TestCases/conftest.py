import pytest
from selenium import webdriver
from Utilities.readProperties import ReadConfig 



driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome")
    


@pytest.fixture(scope="class")
def browserSetup(request):
    browsername = request.config.getoption("browser_name")
    global driver
    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
       
        
    elif browsername == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\drivers\\geckodriver.exe")
        
    driver.get(ReadConfig.getConfigData("appURL"))
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                filename="..\\Screenshots\\"+file_name
                html = '<div><img src="%s" alt="screenshot" style="width:104px;height:55px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % filename
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file("..\\Screenshots\\"+name)


