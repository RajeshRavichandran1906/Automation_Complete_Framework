'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288339'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288339_TestClass(AS_BaseTestCase):
    def test_C2288339(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click FWSubfolder under Domains and select New>SQL Chart. 
                    Click Cancel'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                    
        tree_path="Domains->S9100->FWSubFolder"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="SQL Chart")
        time.sleep(4)
        
        as_utilobj.Verify_Current_Dialog_Opens("SQL Chart Wizard - Welcome","Step 1.1: SQL Report Wizard - Welcome.")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Closes("SQL Report Wizard - Welcome","Step 1.2: Wizard closes. The new sql chart was not added to sub folder in the tree.")
        time.sleep(1)
        
        '''Step 02: Right click FWSubfolder under Domains and select New>HTML/Document
                    Click Cancel'''
                    
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="HTML/Document")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("HTML / Document Wizard","Step 2.1: HTML / Document Wizard Wizard opens - Welcome.")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Closes("HTML / Document Wizard","Step 2.2: Wizard closes. The new HTML/Document was not added to sub folder in the tree")
        time.sleep(1)
        
        '''Step 03: Right click FWSubfolder under Domains and select New>Alert
                    Click X to close Alert - WebFOCUS Alert Assist tab'''

        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="Alert")
        time.sleep(8)
        
        as_utilobj.verify_active_tool("App Studio - Alert - WebFOCUS Alert Assist","Step 3.1: Alert Assist Web tool opens")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio", "Step 3.2: Alert Assist Web tool closes. No new alert file creation")
        time.sleep(1)
        
        '''Step 04: Right click FWSubfolder under Domains and select New>Reporting Object
                    Click X to close ReportingObject- WebFOCUS Reporting Object tab'''

        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="Reporting Object")
        time.sleep(4)
        
        as_utilobj.verify_active_tool("App Studio - ReportingObject - WebFOCUS Reporting Object","Step 4.1: Reporting Object-WebFOCUS Reporting Object Web tool opens.")
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.verify_active_tool("App Studio", "Step 4.2: Reporting Object-WebFOCUS Reporting Object tab closes. No new Reporting Object file creation")
        time.sleep(2)
        
        '''Step 05: Right click FWSubfolder under Domains and select New>URL
                    Click Cancel'''

        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="URL")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("Create URL","Step 5.1: URL Window opens")
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Closes("Create URL","Step 5.2: URL Window closes")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()