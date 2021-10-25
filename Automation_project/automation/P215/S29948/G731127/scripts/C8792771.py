'''
Created on Apr 16, 2019

@author: ml12793
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8792771
Test case title: Create FOCEXEC file,Saved in Repository using Save As dialog 
'''
import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C8792771_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C8792771_TestClass, self).__init__(driver)
    
    def test_C8792771(self):   
        
        case_id = 'C8792771'
        tool = 'text editor'
        
        utilobj = Selenium_Utility(self.driver)
        utilobj.login_wf()    
        
        #Step 1: navigate to case folder
        utilobj.navigate_to_case_folder()   
        
        #Step 2, 3: launch text editor and type fex
        utilobj.launch_text_editor_to_type_fex()
        
        #step 4, 5, 6: save fex
        utilobj.save_fex_as(tool, case_id)
        
        #step 7: exit text editor
        utilobj.exit_tool(tool)
        
        #step 8: right click fex to run, verify output
        utilobj.right_click_item_to_perform('file-item', 'run', case_id)
        utilobj.verify_table(case_id, '8')
        
        #step 9: right click fex to edit 
        utilobj.right_click_item_to_perform('file-item', 'edit', case_id)
        utilobj.verify_fex(case_id, '9')
        
        #step 10: exit the text editor
        utilobj.exit_tool(tool)
              
if __name__ == "__main__":   
    unittest.main()        