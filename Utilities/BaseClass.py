import pytest
from Utilities.customLogger import CustomLogger

@pytest.mark.usefixtures("browserSetup")
class Baseclass:
    
    clogger=CustomLogger()
    
        
   
    
