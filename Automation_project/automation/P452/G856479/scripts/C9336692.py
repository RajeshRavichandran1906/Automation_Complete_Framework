#for local testing
import sys
sys.path.append('../')
#*************************

import unittest
from utility.selenium_utility import Selenium_Utility, ParisHomeUtility, DesignerUtility
from utility.basetestcasedocker import BaseTestCaseDocker

class C9336692_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9336692_TestClass, self).__init__(driver)
    
    def test_C9336692(self):        
        
        case_id = 'C9336692'
        
        sel_util = Selenium_Utility(self.driver)
        
        #Log into WF
        sel_util.login_wf()

#***tested       
#         home_util = ParisHomeUtility(self.driver)
#         
#         #Navigate to work space folder
#         home_util.navigate_to_workspace_folder("Retail Samples")
#         
#         #Create portal - if portal exists, it will be deleted 
#         home_util.create_new_portal("test portal2")
#         
#         #Publish portal
#         home_util.publish_portal_folder("test portal2")
#         
#         self.driver.switch_to.default_content()
#         
#         #Launch Designer by clicking 'Visualize Data'
#         home_util.launch_designer()
        
        self.driver.get("http://bigscm14:8080/ibi_apps8/designer?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FRetail_Samples%2F~admin&BIDrand=654&tool=framework&startlocation=IBFS%3A%2FWFC%2FRepository%2FRetail_Samples%2F~admin&startUpConditions=%7B%27mode%27%3A%27internal%27%7D")
        df_util = DesignerUtility(self.driver)
        
        #Select a master file
        df_util.select_data_source("wf_retail_lite")
        
        
        
              
if __name__ == "__main__":   
    unittest.main()