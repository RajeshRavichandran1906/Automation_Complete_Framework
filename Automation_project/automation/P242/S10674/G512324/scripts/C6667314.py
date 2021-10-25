'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667314'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C6667314_TestClass(AS_BaseTestCase):
    def test_C6667314(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New->Page->OK'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Portal Page")
        time.sleep(25)
        
        as_utilobj.click_element_using_ui(text_click="Create")
        time.sleep(15)
        
        as_utilobj.verify_active_tool("App Studio - Page Designer","Step 01: Verified portal page designer invoked in App studio canvas area")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 1.1: Verify Open button enabled in QAT",button_item="Open...",enabled=True)
        
        qat_toolbar=['Save','Save All','Quick Print','Undo','Redo','Cut','Copy','Paste']
        for buttons in qat_toolbar:
            as_utilobj.verify_element_using_ui("Step 1.1: Verify QAT buttons disabled - " + buttons,button_item=buttons,disabled=True)
          
        as_utilobj.verify_element_using_ui("Step 1.1: Verify QAT buttons Run is disabled",split_button_item="Run",disabled=True)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui("Step 1.1: Verify QAT buttons Customize toolbar button is enabled",split_button_item='Customize Quick Access Toolbar',enabled=True)
        time.sleep(1)
        
        '''Step 02: Close Page Designer tab
                    Click on Leave this page'''
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.select_home_button(move_x=370,move_y=20)
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Windows Internet Explorer","Step 02: Verified portal page closure prompt appears")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Leave this page")
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
                 
if __name__=='__main__' :
    unittest.main()