'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2296369'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2296369_TestClass(AS_BaseTestCase):
    def test_C2296369(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
          
        as_utilobj.select_home_button()
        
        '''Step 01: Click HTML / Document icon in the Home Ribbon'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
               
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
        
        as_utilobj.click_element_using_ui(button_item=True,name="HTML / Document")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("HTML / Document Wizard","Step 01: Verify HTML / Document wizard Opens to create an HTML")
        time.sleep(1)
        
        '''Step 02: Click Next'''
        
        as_utilobj.select_any_dialog("Next >")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Templates, Settings, and Themes","Step 02: Verify HTML / Document wizard Opens Templates, Settings, and Themes section")
        time.sleep(1)
        
        '''Step 03: Click Back, select "Guided Report Page" radio button, click Next'''
        
        as_utilobj.select_any_dialog("< Back")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(radio_button="23560")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Next >")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Templates, Settings, and Themes","Step 03: Verify HTML / Document wizard Opens guided report page - Templates, Settings, and Themes section")
        time.sleep(1)
        
        '''Step 04: Click Back, select "Document (PDF, Excel...)" radio button, click Next'''
        
        as_utilobj.select_any_dialog("< Back")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(radio_button="23561")
        time.sleep(1) 
        
        as_utilobj.select_any_dialog("Next >")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("HTML / Document Wizard","Step 04: Verify HTML / Document wizard Opens to create and Document")
        time.sleep(1)
        
        '''Step 05: Click Cancel'''
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 